from modeltranslation.translator import translator, TranslationOptions
from .models import Category, ProductClass, Product


class CategoryTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Category.
    """
    fields = ('name', 'description',)


class ProductClassTranslationOptions(TranslationOptions):
    fields = ('name',)

class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(ProductClass, ProductClassTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
