from modeltranslation.translator import translator, TranslationOptions
from apps.catalogue.models import Category


class CategoryTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Category.
    """

    fields = ('name', 'description',)


translator.register(Category, CategoryTranslationOptions)