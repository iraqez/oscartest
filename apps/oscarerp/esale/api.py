from django.contrib.sites.models import Site
from django.core.files.base import ContentFile
from django.db.models import get_model
from django.conf import settings
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, SessionAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from oscar.apps.catalogue.models import Category, ProductClass, Product, ProductCategory, ProductRecommendation, ProductImage
from oscar.apps.partner.models import Partner, StockRecord
import urllib2

class StaffAuthorization(DjangoAuthorization):

    def base_checks(self, request, model_klass):
        # If it doesn't look like a model, we can't check permissions.
        if not model_klass or not getattr(model_klass, '_meta', None):
            return False

        # User must be logged in to check permissions.
        if not hasattr(request, 'user'):
            return False

        if request and hasattr(request, 'user'):
            if not request.user.is_staff:
                return False

        return model_klass


class SiteResource(ModelResource):

    class Meta:
        queryset = Site.objects.filter(id=settings.SITE_ID)
        resource_name = 'site'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()


class PartnerResource(ModelResource):

    class Meta:
        queryset = Partner.objects.filter()
        resource_name = 'partner'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()
        filtering = {
            "code": ('exact',),
        }


class CategoryResource(ModelResource):
    #~ products = fields.ToManyField('esale.api.ProductResource', related_name='categories')

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()

    def obj_create(self, bundle, **kwargs):

        # Calculate path category number
        steplen = 4
        key = bundle.data.get('sequence')
        if bundle.data.get('parent_id'):
            parent_id = bundle.data.get('parent_id')
            parent = Category.objects.get(id=parent_id)
            path = '%s%s%s' % (parent.path, '0' * (steplen - len(str(key))), key)
            del bundle.data['parent_id']
        else:
            path = '%s%s' % ('0' * (steplen - len(str(key))), key)

        bundle.data['path'] = path

        return super(CategoryResource, self).obj_create(bundle, **kwargs)


class ProductClassResource(ModelResource):

    class Meta:
        queryset = ProductClass.objects.all()
        resource_name = 'productclass'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()


class ProductResource(ModelResource):
    product_class = fields.ForeignKey(ProductClassResource, 'product_class')
    #~ categories = fields.ManyToManyField(CategoryResource, 'categories', full=False, null=True)
    #~ categories = fields.ManyToManyField(CategoryResource, 'categories', full=True, null=True)
    #~ categories = fields.ToManyField(CategoryResource, attribute=lambda bundle: Category.objects.filter(name=bundle.obj, name__startswith='Categories'), null=True)
    #~ through_query = lambda bundle: bundle.obj.categories.through.objects.all()
    #~ categories = fields.ToManyField(CategoryResource, attribute=through_query, full=False, null=True)

    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()
        filtering = {
            "upc": ('exact',),
        }

    def obj_create(self, bundle, **kwargs):
        id = bundle.data['id']

        categories = bundle.data.get('categories')
        if categories:
            del bundle.data['categories']

        recommendations = bundle.data.get('recommendations')
        if recommendations:
            del bundle.data['recommendations']

        product_bundle = super(ProductResource, self).obj_create(bundle, **kwargs)

        product = Product.objects.get(id=id)

        ProductCategory.objects.filter(product=id).delete()
        if categories:
            for cat in categories:
                category = Category.objects.get(id=cat)
                productcategory = ProductCategory()
                productcategory.product = product
                productcategory.category = category
                productcategory.save()

        ProductRecommendation.objects.filter(primary=id).delete()
        if recommendations:
            for r in recommendations:
                recommendation = Product.objects.get(id=r)
                productrecommendation = ProductRecommendation()
                productrecommendation.primary = product
                productrecommendation.recommendation = recommendation
                productrecommendation.save()

        return product_bundle

    def save_m2m(self, bundle):
        return bundle


class ProductInfoResource(ModelResource):
    product_class = fields.ForeignKey(ProductClassResource, 'product_class')
    categories = fields.ManyToManyField(CategoryResource, 'categories', full=False, null=True)

    class Meta:
        queryset = Product.objects.all()
        resource_name = 'productinfo'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()


class ProductImageResource(ModelResource):

    class Meta:
        queryset = ProductImage.objects.all()
        resource_name = 'productimage'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()

    def obj_create(self, bundle, **kwargs):

        ProductImage = get_model('catalogue', 'ProductImage')

        product = Product.objects.get(id=bundle.data.get('product'))
        if not product:
            return bundle

        image_url = bundle.data.get('image')
        image_data = urllib2.urlopen(image_url, timeout=5)
        filename = image_url.split('/')[-1]

        i = ProductImage.objects.filter(original__endswith=filename)
        if i:
            image = i[0]
        else:
            image = ProductImage()

        image.product = product
        image.caption = bundle.data.get('caption')
        image.display_order = bundle.data.get('order', 0)
        image.active = bundle.data.get('active', True)

        image.original = filename
        image.original.save(
            filename,
            ContentFile(image_data.read()),
            save=False
        )
        image.save()

        return bundle

class StockRecordResource(ModelResource):
    product = fields.ForeignKey(ProductResource, 'product')
    partner = fields.ForeignKey(PartnerResource, 'partner')

    class Meta:
        queryset = StockRecord.objects.all()
        resource_name = 'stockrecord'
        authentication = MultiAuthentication(SessionAuthentication(), BasicAuthentication())
        authorization = StaffAuthorization()
        filtering = {
            "partner_sku": ('exact',),
        }
