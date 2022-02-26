from email.mime import image
from msilib.schema import tables
from django.shortcuts import render,redirect,get_object_or_404
import json
from django.views import generic

from blog.editorjs import editorjs
from . import blogconfig
from django.core.files.storage import default_storage
from .models import Post,category
from django.contrib import messages
from django.forms import ModelForm
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
def home(request):
    all_stories = Post.objects.values("title","slug","meta_description","thumbnail","author","updated_on").filter(status=1).order_by('-updated_on')[:6]
    category_featured = category.objects.values('id','category_name').get(category_name="Featured")
    featured = Post.objects.values("title","slug","meta_description","thumbnail","author","updated_on").filter(status=1).order_by('-updated_on').filter(categorys=category_featured['id'])[:4]
    return render(request, 'index.html',{'siteconfig':blogconfig.Site,'featured':featured,'all_stories':all_stories})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['siteconfig'] = blogconfig.Site
        body=context['object'].body
        body = editorjs(body)
        context['siteurl']=context['object'].get_absolute_url()
        category_recommended = context['object'].categorys.all().values('id')
        context['recommended']=Post.objects.distinct().values("title","slug","meta_description","thumbnail","author","updated_on").filter(status=1).order_by('-updated_on').filter(categorys__in=category_recommended)[:10]
        context['body'] =body
        return context


#------------------------------------------------start editor.js views---------------------------------------------------------
@requires_csrf_token
def uploadi(request):
    f=request.FILES['image']
    fs=default_storage
    filename=str(f)
    file= fs.save(filename,f)
    fileurl=fs.url(file)
    return JsonResponse({'success':1,'file':{'url':fileurl}})

@requires_csrf_token
def uploadf(request):
    f=request.FILES['file']
    fs=default_storage
    filename,ext=str(f).split('.')
    print(filename,ext)
    file=fs.save(str(f),f)
    fileurl=fs.url(file)
    fileSize=fs.size(file)
    return JsonResponse({'success':1,'file':{'url':fileurl,'name':str(f),'size':fileSize}})

def upload_link_view(request):
    import requests
    from bs4 import BeautifulSoup  
    print(request.GET['url'])
    url = request.GET['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text,features="html.parser")
    metas = soup.find_all('meta')
    description=""
    title=""
    image=""
    for meta in metas:
        if 'property' in meta.attrs:
            if (meta.attrs['property']=='og:image'):
                image=meta.attrs['content']         
        elif 'name' in meta.attrs:         
            if (meta.attrs['name']=='description'):
                description=meta.attrs['content']
            if (meta.attrs['name']=='title'):
                title=meta.attrs['content']
    return JsonResponse({'success':1,'meta':{"description":description,"title":title, "image":{"url":image}}})

#------------------------------------------------end editor.js views---------------------------------------------------------

