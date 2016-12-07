from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractCategory, AbstractProductClass,\
    AbstractProduct, AbstractProductAttribute, AbstractProductAttributeValue,\
    AbstractAttributeOptionGroup, AbstractAttributeOption
from django.utils.translation import ugettext_lazy as _

# __all__ = ['ProductAttributesContainer']



class ProductClass(AbstractProductClass):
    pass

class Category(AbstractCategory):
    metatag_keyworlds = models.CharField(verbose_name=_('Keyword'), max_length=255, null=True)


class Product(AbstractProduct):
   metatag_keyworlds = models.CharField(verbose_name=_('Keyword'), max_length=255, null=True)


class ProductAttribute(AbstractProductAttribute):
    pass

class ProductAttributeValue(AbstractProductAttributeValue):
    pass

class AttributeOption(AbstractAttributeOption):
    pass

class AttributeOptionGroup(AbstractAttributeOptionGroup):
    pass

from oscar.apps.catalogue.models import *  # noqa