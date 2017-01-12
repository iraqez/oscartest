from decimal import Decimal as D
from oscar.apps.shipping.methods import Free, NoShippingRequired
from esale.apps.shipping.methods import *
from oscar.apps.shipping.repository import Repository as CoreRepository
from oscar.apps.address.models import UserAddress
from django.conf import settings
from esale.apps.esale.erp import *

import erppeek
from proteus import config, Model


class Repository(CoreRepository):

    def get_shippings(self, basket, postcode=None, country=None, state=None):
        total = float(self.get_total(basket))
        weight = self.get_weight( basket)
        shop = settings.OSCAR_ERP_SHOP

        if settings.OSCAR_ERP == 'openerp':
            Client = openerp_connect()
            deliveries = Client.execute('sale.shop', 'oscar_deliveries',
                            shop, total, weight, postcode, country, state)

        if settings.OSCAR_ERP == 'tryton':
            dliveries = [] #  TODO

        return deliveries

    def get_total(self, basket):
        return basket.total_incl_tax

    def get_weight(self, basket):
        #~ for line in basket.lines:
            # TODO Add weight field in product and process all lines basket and calculate weight
        return 0 

    def get_shipping_methods(self, user, basket, shipping_addr=None, **kwargs):
        methods = []
        postcode = None
        country = None
        state = None

        if shipping_addr:
            postcode = shipping_addr.postcode
            country = shipping_addr.country.iso_3166_1_a2
            state = shipping_addr.state

        for delivery in self.get_shippings(basket, postcode, country, state):
            if delivery.get('code') == 'free-shipping':
                methods.append(Free())
                continue

            code = delivery.get('code')
            name = delivery.get('name')
            charge_incl_tax = decimal.Decimal(delivery.get('charge_incl_tax'))
            charge_excl_tax = decimal.Decimal(delivery.get('charge_excl_tax'))
            methods.append(ErpShipping(code, name, charge_incl_tax, charge_excl_tax))
        return self.prime_methods(basket, methods)

    def find_by_code(self, code, basket, address):
        # -----------------------------------------------------------
        # get country, state and postcode to calculate shipping price
        # -----------------------------------------------------------
        postcode = None
        country = None
        state = None
        if isinstance(address, int) or isinstance(address, long):
            useraddress = UserAddress._default_manager.filter(user=address)
            if useraddress:
                postcode = useraddress[0].postcode
                country = useraddress[0].country.iso_3166_1_a2
                state = useraddress[0].state
        else:
            postcode = address.get('postcode', None)
            if address.get('country'):
                country = address.get('country').iso_3166_1_a2
            state = address.get('state', None)

        # ------------
        # Load methods
        # ------------
        method = Free()
        if code == Free.code:
            method = Free()
        else:
            for delivery in self.get_shippings(basket, postcode, country, state):
                if delivery.get('code') == code:
                    name = delivery.get('name')
                    charge_incl_tax = decimal.Decimal(delivery.get('charge_incl_tax'))
                    charge_excl_tax = decimal.Decimal(delivery.get('charge_excl_tax'))
                    method = ErpShipping(code, name, charge_incl_tax, charge_excl_tax)
        return self.prime_method(basket, method)
