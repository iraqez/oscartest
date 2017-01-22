import csv
import re
from decimal import Decimal

from oscar.apps.catalogue.models import Product, Category, ProductAttribute,\
                                        ProductClass, ProductCategory,\
                                        ProductAttributeValue
from oscar.apps.partner.models import Partner, StockRecord

#from utils import get_canonical_product_code

"""
Example of CSV file contents:

BEANS,,,,,,,,,
BEADZ5.1.2,Adzuki Beans 1.2KG,HTG,6,$6.9,$4.93,N,,Australia,
BEADZ5.25,Adzuki Beans 25kg,Bulk,1,$71.5,,N,,Australia,
BEADZ5.5,Adzuki Beans 5kg,Bulk,1,$17.8,,N,,Australia,
BEBLAT5.5,Black Turtle Beans 5kg,Bulk,1,$19.75,,N,,Canada,
BEBLAT5.25,Black Turtle Beans 25kg,Bulk,1,$81.25,,N,,Canada,
BEBOR5.25,Borlotti Beans 25kg,Bulk,1,$104,,N,,Australia,
BEBOR5.5,Borlotti Beans 5kg,Bulk,1,$24.3,,N,,Australia,

"""

partner = Partner.objects.filter(name='HTG')
if partner.exists():
    partner = partner[0]
else:
    partner = Partner()
    partner.name = 'Импортированный поставщик'
    partner.save()

product_class = ProductClass.objects.filter(name='Еда')
if product_class.exists():
    product_class = product_class[0]
else:
    product_class = ProductClass()
    product_class.name = 'Еда'
    product_class.track_stock = False
    product_class.save()

pa_weight = ProductAttribute.objects.filter(name='вес')
if pa_weight.exists():
    pa_weight = pa_weight[0]
else:
    pa_weight = ProductAttribute()
    pa_weight.name = 'вес'
    pa_weight.save()

pa_gst = ProductAttribute.objects.filter(name='GST')
if pa_gst.exists():
    pa_gst = pa_gst[0]
else:
    pa_gst = ProductAttribute()
    pa_gst.name = 'GST'
    pa_gst.save()

categories = {
    'BE': 'Beans',
    'BI': 'Baking ingredients',
    'CE': 'Cereals',
    # etc
}


def init_or_get_category(cat_key):
    """Loads existing category from DB or creates a new one"""

    if categories.has_key(cat_key):
        category = categories[cat_key]
        # Create or load existing category
        if type(category) == str:
            cat_name = categories[cat_key]
            if Category.objects.filter(name=cat_name).exists():
                category = Category.objects.get(name=cat_name)
            else:
                #category = root_category.add_child(name=cat_name)
                category = Category.add_root(name=cat_name)
            categories[cat_key] = category
        return category
    else:
        return None


def get_title_and_weight(raw_title):
    """Extracts title and weight from the original title in the data"""
    pos = re.search('\d+\.?\d*KG', raw_title, flags=re.IGNORECASE)
    if pos is None:
        return (raw_title, None)
    else:
        return (raw_title[:pos.start()], raw_title[pos.start():])


def get_or_create_canonical_product(name, title, category):

    canonical_name = get_canonical_product_code(name)
    if canonical_name is None:
        print('Cannot get canonical code from ', name, ', skipping')
        return None

    product = Product.objects.filter(upc=canonical_name)
    if not product.exists():
        product = Product()
        product.upc = canonical_name

        product.title, weight = get_title_and_weight(title)

        product.product_class = product_class
        product.save()

        # Associate with a category
        cat_prod = ProductCategory()
        cat_prod.product = product
        cat_prod.category = category
        cat_prod.is_canonical = True
        cat_prod.save()

    else:
        product = product[0]

    return product

#
# Start processing CSV
#
with open('feb.csv', 'rb') as f:
    pricelist_reader = csv.reader(f, delimiter=',')

    for row in pricelist_reader:
        # Skip empty lines / Category name rows in CSV
        if len(row[0]) == 0 or len(row[1]) == 0:
            continue
        #
        # Cells are in the following order:
        # Code,Product,Brand,Unit per box,Single unit price,"Unit price for box buy",GST,Org Cert,Origin,Comments
        #
        cat_key = row[0][0:2].upper()
        category = init_or_get_category(cat_key)

        if category is None:
            print('Unknown category for product code ', row[0])
            continue

        canonical_product = get_or_create_canonical_product(name=row[0],
                                                            title=row[1],
                                                            category=category)
        if canonical_product is None:
            continue

        p_var = Product.objects.filter(upc=row[0])
        if p_var.exists():
            continue
        else:
            title, weight = get_title_and_weight(row[0])

            p_var = Product()
            p_var.parent = canonical_product
            p_var.upc = row[0]
            p_var.title = row[1]
            p_var.product_class = product_class
            p_var.save()

            # Associate with a category
            cat_prod = ProductCategory()
            cat_prod.product = p_var
            cat_prod.category = category
            cat_prod.save()

            #Set weight attribute
            weight_attr = ProductAttributeValue()
            weight_attr.product = p_var
            weight_attr.attribute = pa_weight
            weight_attr.value_text = weight
            weight_attr.save()

            #Set GST attribute
            gst_attr = ProductAttributeValue()
            gst_attr.product = p_var
            gst_attr.attribute = pa_gst
            gst_attr.value_boolean = row[6].lower() == 'y'
            gst_attr.save()

            # Set the price
            rec = StockRecord()
            rec.product = p_var
            rec.partner = partner
            rec.partner_sku = p_var.upc

            price = row[4]
            if len(price) == 0:
                print('No price ', row)
                continue
            if price[0] == '$':
                price = price[1:]
            rec.price_excl_tax = Decimal(price)
            rec.save()