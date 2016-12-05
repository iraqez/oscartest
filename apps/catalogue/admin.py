from django.contrib import admin
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

admin.site.register(CategoryNew, CategoryAdminI18n)
from oscar.apps.catalogue.admin import *  # noqa

#