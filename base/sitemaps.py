from msilib.schema import Class
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    
    def items(self):
        return Post.objects.filter(status=1)
    def lastmod(self, obj):
        return obj.updated_on
class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['home', 'post', 'author']

    def location(self, item):
        return reverse(item)
