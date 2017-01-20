from decimal import Decimal
from trytond import backend

from proteus import config, Model

config = config.set_trytond('tryton', user='admin', config_file='./trytond.conf')

Product = Model.get('product.product')
ProductTemplate = Model.get('product.template')
Category = Model.get('product.category')
ProductUom = Model.get('product.uom')
AccountCategory = Model.get('product.template-product.category')

category, = Category.find([('name', '=', 'Baby')])
unit, = ProductUom.find([('id', '=', '1')])
# account, = AccountCategory.find([('id', '=', '2')])

line = ['Картина "Пьяная сова"', '70.47', '34.89']
def LoadProducts():
    header=False
    if not header:
        print(line[0])
        pt = ProductTemplate()
        pt.name = line[0]
        pt.list_price = Decimal(line[1])
        pt.cost_price = Decimal(line[2])
        pt.category = category
        pt.default_uom = unit
        pt.type = 'goods'
        pt.purchasable = False
        pt.salable = False
        pt.account_category = None
        pt.taxes_category = False
        pt.code = 'code'
        pt.manufacter_code = 'manufacter_code'
        pt.save()

        product = Product(template=pt)
        product.save()
    header=False

if __name__ == "__main__":
  LoadProducts()
