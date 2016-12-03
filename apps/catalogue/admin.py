from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category
from oscar.apps.catalogue.admin import CategoryAdmin as CoreCategoryAdmin
from oscar.apps.catalogue.admin import *  # noqa
#

class CategoryAdmin(CoreCategoryAdmin, TranslationAdmin):

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

from oscar.apps.catalogue.admin import *  # noqa

