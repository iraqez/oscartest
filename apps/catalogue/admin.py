from django.contrib import admin
<<<<<<< HEAD
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
=======
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Category as CategoryNew
from oscar.apps.catalogue.admin import Category as CategoryOld  # noqa
import apps.catalogue.translation

admin.site.unregister(CategoryOld)
#admin.site.register(CatNew)
class CategoryAdminI18n(TreeAdmin, TabbedTranslationAdmin):
    form = movenodeform_factory(CategoryOld)
    list_display = ('name', 'name_ru', 'name_uk', 'slug')
    list_filter = ('name_ru', 'name_uk')
>>>>>>> 9ec7991faf83d44bbde70411ae250c47bf8af4b3

admin.site.register(CategoryNew, CategoryAdminI18n)
from oscar.apps.catalogue.admin import *  # noqa

