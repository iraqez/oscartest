from django.conf import settings
from django.http import Http404
import socket
from django.http import HttpResponse

import erppeek
from proteus import config, Model

def openerp_connect():
    '''OpenERP Connection'''
    try:
        Client = erppeek.Client(
            settings.OSCAR_ERP_SERVER,
            db=settings.OSCAR_ERP_DATABASE,
            user=settings.OSCAR_ERP_USERNAME,
            password=settings.OSCAR_ERP_PASSWORD
            )
    except socket.error:
        raise Exception("Not available OpenERP connection. Check if OpenERP server is up")
    except:
        raise Exception("Not available OpenERP connection. Check if OpenERP server is up")
    return Client

def tryton_connect():
    '''Tryton Connection'''
    # TODO
    return None
