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
    #next(item for item in categories if item["parent_id"] == "2")
    for i in cat:
        if i['parent_id'] == '2':
            if Category.objects.filter(id=i['id']).exists():
                pass
            else:
                Category.add_root(name=i['name'], id=i['id'])
                pass
        else:
            if Category.objects.filter(id=i['id']).exists():
                pass
            else:
                x = next(item for item in categories if item["id"] == i['parent_id'])
                print(x)
