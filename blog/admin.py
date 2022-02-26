from django.utils.safestring import mark_safe

from django.contrib import admin
from .models import *
from . import blogconfig


class postAdmin(admin.ModelAdmin):
    def posturl(self, obj=None):
        if obj:
            btn_id = 'copy-helper'
            return mark_safe(f"""
            <input text="text" id="{btn_id}" value="blog/{obj.slug}" style="position: absolute; top: -10000px">
            <a href="#" onclick="document.querySelector(\'#{btn_id}\').select(); document.execCommand(\'copy\');" class="addlink">Copy post url to clipboard</a>
            """
            )
        else:
            return ' '
    posturl.short_description = 'post url '

    def get_readonley_fields(obj=None):
        if obj:
            return ["created_on", "updated_on"]
        else:
            return []

    filter_horizontal = ('categorys',)

    fieldsets = (
        (None, {
            'fields': ('title','slug', 'thumbnail', 'meta_description',)
        }),
        ('blog content', {
            'classes': ('collapse',),
            'fields': ('status','body'),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('posturl','author', 'categorys','created_on', 'updated_on'),
        }),
    )

    
    readonly_fields = ['posturl','created_on', 'updated_on']
    list_display = ('slug','title','status','author',)
    search_fields = ['slug','title',]
    list_filter = ("status",)
    prepopulated_fields = {'slug': ('title',),}
    

admin.site.register(Post,postAdmin)
admin.site.register(category)
# admin.site.register(Imagetable)

# Register your models here.
