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
    def parentID(x):
        if Category.objects.filter(id=x['parent_id']).exists():
            root_category = Category.objects.get(id=x['parent_id'])
            child_category = root_category.add_child(name=x['name'], id=x['id'])
        else:
            def pID(parent):
                parent = x['parent_id']
                for i in categories:
                    if i['id'] == parent:
                        return i

            parentID(pID())

            x = parentID(i['parent_id'])

    for i in cat:
        while i['parent_id'] == '2':
            if Category.objects.filter(id=i['id']).exists():
                continue
            else:
                Category.add_root(name=i['name'], id=i['id'])
            continue
        else:
            if Category.objects.filter(id=i['id']).exists():
                continue
            else:
                parentID(i)