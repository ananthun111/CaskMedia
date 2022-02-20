from msilib.schema import Class
from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1)
    def lastmod(self, obj):
        return obj.updated_on

