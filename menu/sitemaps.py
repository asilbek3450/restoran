from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from menu.models import Product, Category

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'menu', 'about', 'reservation', 'contact']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Product.objects.filter(is_available=True)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('product_detail', kwargs={'slug': obj.slug})

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('menu_category', kwargs={'slug': obj.slug})
