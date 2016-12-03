from oscar.apps.dashboard.catalogue.forms import *  # noqa
from apps.catalogue.models import Category

Category = get_model('catalogue', 'Category')

CategoryForm = movenodeform_factory(
    Category,
    fields=[
        'name', 'description', 'image', 'metatag_keyworlds',
    ])