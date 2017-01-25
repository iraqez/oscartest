import re
from decimal import Decimal
from oscar.apps.catalogue.categories import create_from_breadcrumbs

from apps.catalogue.models import Product, Category, ProductAttribute,\
                                        ProductClass, ProductCategory,\
                                        ProductAttributeValue
from oscar.apps.partner.models import Partner, StockRecord
from .fromRikato import data

#for add Category
#https://github.com/django-oscar/django-oscar/blob/master/tests/integration/catalogue/category_tests.py

categories = data['categories']
products = data['goods']



def category_parent(cat):
    for i in cat:
        if i['parent_id'] == '2':
            if Category.objects.filter(name=i['name']).exists():
                pass
            else:
                Category.add_root(name=i['name'])
        else:
            pass


def add_category(cat):
    for category in cat:
        if Category.objects.filter(name=category['name']).exists():
            print(category['name'])
        else:
            pass
            #Category.objects.get(id=category['id'])
