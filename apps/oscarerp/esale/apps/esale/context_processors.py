from django.conf import settings
from django.utils.translation import get_language

def meta_description(request):
    meta_description = settings.OSCAR_METADESCRIPTION.get(get_language(), '')
    return {'META_DESCRIPTION': meta_description}
