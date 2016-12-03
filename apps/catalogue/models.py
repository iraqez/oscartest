from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractCategory
from django.utils.translation import ugettext_lazy as _

class Category(AbstractCategory):
    metatag_keyworlds = models.CharField(verbose_name=_('Keyword'), max_length=255, null=True)




from oscar.apps.catalogue.models import *  # noqa