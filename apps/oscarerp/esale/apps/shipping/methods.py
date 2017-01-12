from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from oscar.apps.shipping.models import ShippingMethod
from esale.apps.esale.erp import *
import decimal

import erppeek
from proteus import config, Model


class ErpShipping(ShippingMethod):

    def __init__(self, code, name, charge_incl_tax, charge_excl_tax):
        self.code = code
        self.name = name
        self.charge_incl_tax = charge_incl_tax
        self.charge_excl_tax = charge_excl_tax

    def basket_charge_incl_tax(self):
        return self.charge_incl_tax

    def basket_charge_excl_tax(self):
        return self.charge_excl_tax
