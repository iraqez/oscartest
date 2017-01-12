#This file is part django_oscar_erp app for Django.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from django.contrib.sitemaps import Sitemap

from flatpages_i18n.models import FlatPage_i18n
from oscar.apps.catalogue.models import Category, Product


class FlatPage_i18nSitemap(Sitemap):
    """FlatPage i18n Sitemap """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return FlatPage_i18n.objects.filter()


class CategorySitemap(Sitemap):
    """Category Sitemap """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.filter()


class ProductSitemap(Sitemap):
    """Product Sitemap """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.filter()

sitemaps = {
    'flatpage_i18n': FlatPage_i18nSitemap(),
    'product': ProductSitemap(),
    'category': CategorySitemap(),
}
