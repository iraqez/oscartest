import re
from decimal import Decimal
from oscar.apps.catalogue.categories import create_from_breadcrumbs

from apps.catalogue.models import Product, Category, ProductAttribute,\
                                        ProductClass, ProductCategory,\
                                        ProductAttributeValue
from oscar.apps.partner.models import Partner, StockRecord
from importProduct.fromRikato import data

#for add Category
#https://github.com/django-oscar/django-oscar/blob/master/tests/integration/catalogue/category_tests.py

categories = data['categories']
products = data['goods']



def category_parent(cat):
    def parentID(p_id):
        for x in categories:
            if x['id'] == str(p_id):
                return x
                break

    for i in cat:
        if i['parent_id'] == '2':
            if Category.objects.filter(id=i['id']).exists():
                pass
            else:
                Category.add_root(name=i['name'], id=i['id'])
        else:
            if Category.objects.filter(id=i['id']).exists():
                pass
            else:
                if Category.objects.filter(id=i['parent_id']).exists():
                    root_category = Category.objects.get(id=i['parent_id'])
                    child_category = root_category.add_child(name=i['name'], id=i['id'])
                else:
                    x = parentID(i['parent_id'])
