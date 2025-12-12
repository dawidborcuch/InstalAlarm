from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ZdjecieRealizacji


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['index', 'realizacje', 'polityka_prywatnosci']

    def location(self, item):
        return reverse(item)


class RealizacjeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ZdjecieRealizacji.objects.filter(aktywna=True)

    def lastmod(self, obj):
        return obj.data_dodania

