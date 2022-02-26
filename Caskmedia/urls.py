"""Caskmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import views
from base.sitemaps import PostSitemap ,StaticViewSitemap
from django.views.generic.base import TemplateView



blogSitemaps = {
    'static' : StaticViewSitemap,
}
newssitemaps ={
    'news': PostSitemap,
}
Sitemaps =blogSitemaps.copy()
Sitemaps.update(newssitemaps)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', views.index, {'sitemaps': Sitemaps}, name='django.contrib.sitemaps.views.index'),
    path('news/sitemap.xml', views.index, {'sitemaps': newssitemaps,'sitemap_url_name':'django.contrib.sitemaps.views.sitemap.news'}, name='django.contrib.sitemaps.views.index.news'),
    path('news/sitemap-<section>.xml', views.sitemap, {'sitemaps': newssitemaps,'template_name' : 'newssitemap.xml','content_type':'application/xml'}, name='django.contrib.sitemaps.views.sitemap.news'),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': Sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('',include('blog.urls')),
    path('',include('base.urls')),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    ]