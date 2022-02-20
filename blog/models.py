from enum import unique
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_editorjs import EditorJsField


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Imagetable(models.Model):
    image = models.ImageField(upload_to="images/uploads/")

class category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name
    class Meta:
        db_table = 'category'
        ordering = ['id']

class Post(models.Model):
    title = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = EditorJsField(
        editorjs_config={
            "tools":{
                "Checklist":{
                    "disabled": True,
                },

                "Link":{
                    "config":{
                        "endpoint":
                            '/linkfetching/'
                        }
                },
                "Image":{
                    "config":{
                        "endpoints":{
                            "byFile":'/uploadi/',
                            "byUrl":'/uploadi/'
                        },
                       
                    }
                },
                "Attaches":{
                    "disabled": True,
                    "config":{
                        "endpoint":'/uploadf/'
                    }
                }
            }
        }
    )
    thumbnail = models.ImageField(upload_to="thumbnail/uploads/",height_field=None, width_field=None)
    meta_description = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categorys = models.ManyToManyField(category,blank=True,related_name='categorys')

    class Meta:
        db_table = 'Post'
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])
    