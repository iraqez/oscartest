#This file is part django_oscar_erp app for Django.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap

from oscar.app import application
from oscar.views import handler500, handler404, handler403
from esale.app import application
from sitemaps import sitemaps

from tastypie.api import Api
from esale.api import (SiteResource, PartnerResource, StockRecordResource,
                        CategoryResource, ProductClassResource, ProductResource, ProductInfoResource, ProductImageResource)

v1_api = Api(api_name='v1')
v1_api.register(SiteResource())
v1_api.register(PartnerResource())
v1_api.register(CategoryResource())
v1_api.register(ProductClassResource())
v1_api.register(ProductResource())
v1_api.register(ProductInfoResource())
v1_api.register(ProductImageResource())
v1_api.register(StockRecordResource())

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^api/', include(v1_api.urls)),
    (r'', include(application.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
