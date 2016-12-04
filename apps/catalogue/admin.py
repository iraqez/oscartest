from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category
from oscar.apps.catalogue.admin import CategoryAdmin as CoreCategoryAdmin
from oscar.apps.catalogue.admin import *  # noqa


class CoreCategoryAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'tabbed_translation_fields.js',
        )
        css = {
            'screen': ('tabbed_translation_fields.css',),
        }

from oscar.apps.catalogue.admin import *  # noqa

