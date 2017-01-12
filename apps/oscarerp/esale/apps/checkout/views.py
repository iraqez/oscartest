from django.http import HttpResponseRedirect
from django.db.models import get_model
from django.conf import settings
from oscar.apps.checkout import views
from esale.apps.esale.erp import *

import re
import threading
import erppeek
from proteus import config, Model

ShippingAddress = get_model('order', 'ShippingAddress')


class PaymentDetailsView(views.PaymentDetailsView):

    def str_az09(self, string):
        '''Convert character alphanumeric'''
        if not string:
            return
        string = re.sub('[^a-zA-Z0-9 -]', '', string)
        return string.title()

    def oscar2erp_data(self, order):
        '''Data Oscar order to dict'''
        # =====
        # Order
        # =====
        sale_order = {}
        sale_order['number'] = order.number
        sale_order['email'] = order.email
        sale_order['date'] = order.date_placed.strftime('%Y-%m-%d %H:%M:%S')
        sale_order['total_incl_tax'] = str(order.total_incl_tax)
        sale_order['total_excl_tax'] = str(order.total_excl_tax)
        sale_order['shipping_incl_tax'] = str(order.shipping_incl_tax)
        sale_order['shipping_excl_tax'] = str(order.shipping_excl_tax)
        sale_order['shipping_method'] = order.shipping_method

        # =======
        # Address
        # =======
        vat = self.str_az09(address.vat)
        if vat:
            vat = vat.upper()

        address = ShippingAddress.objects.get(id=order.shipping_address.id)
        shipping_address = {}
        shipping_address['first_name'] = self.str_az09(address.first_name)
        shipping_address['last_name'] = self.str_az09(address.last_name)
        shipping_address['full_name'] = self.str_az09(order.shipping_address.name())
        shipping_address['vat'] = vat
        shipping_address['line1'] = self.str_az09(address.line1)
        shipping_address['line2'] = self.str_az09(address.line2)
        shipping_address['line3'] = self.str_az09(address.line3)
        shipping_address['city'] = self.str_az09(address.line4)
        shipping_address['state'] = self.str_az09(address.state)
        shipping_address['postcode'] = address.postcode
        shipping_address['country'] = order.shipping_address.country.iso_3166_1_a2
        shipping_address['phone_number'] = order.shipping_address.phone_number
        sale_order['address'] = shipping_address

        # =====
        # Lines
        # =====
        lines = []
        for line in order.lines.all():
            lines.append({
                'upc': line.upc,
                'name': line.title,
                'quantity': line.quantity,
                'price_before_discounts_incl_tax': str(line.line_price_before_discounts_incl_tax),
                'price_before_discounts_excl_tax': str(line.line_price_before_discounts_excl_tax),
                'price_incl_tax': str(line.line_price_incl_tax),
                'price_excl_tax': str(line.line_price_excl_tax),
                })
        sale_order['lines'] = lines

        # ========
        # Discount
        # ========
        discounts = []
        for discount in order.discounts.all():
            discounts.append({
                'name': discount.offer_name,
                'price': str(discount.amount),
                })
        sale_order['discounts'] = discounts

        # =======
        # Payment
        # =======
        payments = []
        payment = None
        for source in order.sources.all():
            payments.append(source)
        if payments:
            payment = payments[0]
        if payment:
            sale_order['payment'] = payment

        # =====
        # Notes
        # =====
        sale_order['notes'] = order.shipping_address.notes

        return sale_order

    def oscar2erp(self, data):
        '''Send order values to ERP'''
        shop = settings.OSCAR_ERP_SHOP

        if settings.OSCAR_ERP == 'openerp':
            Client = openerp_connect()
            Client.execute('sale.shop', 'oscar_create_order', shop, data)

        #~ if settings.OSCAR_ERP == 'tryton':
            # TODO call tryton proteus to send data

        return True

    def handle_successful_order(self, order):
        # Send confirmation message (normally an email)
        self.send_confirmation_message(order)

        # Flush all session data
        self.checkout_session.flush()

        # Save order id in session so thank-you page can load it
        self.request.session['checkout_order_id'] = order.id

        # Send order to ERP with thread
        data = self.oscar2erp_data(order)
        thread1 = threading.Thread(target=self.oscar2erp, args=[data])
        thread1.start()

        response = HttpResponseRedirect(self.get_success_url())
        self.send_signal(self.request, response, order)
        return response

    #~ def handle_payment(self, order_number, total_incl_tax, **kwargs):
        # Create a payment event
        # self.add_payment_event('Authorize', total_incl_tax)
