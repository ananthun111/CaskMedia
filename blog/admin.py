from django.utils.safestring import mark_safe

from django.contrib import admin
from .models import *
from . import blogconfig


class postAdmin(admin.ModelAdmin):
    def posturl(self,obj):
        btn_id = 'copy-helper'
        return mark_safe(f"""
        <input text="text" id="{btn_id}" value="{blogconfig.Site['host']+'blog/'+obj.slug}" style="position: absolute; top: -10000px">
        <a href="#" onclick="document.querySelector(\'#{btn_id}\').select(); document.execCommand(\'copy\');" class="addlink">Copy post url to clipboard</a>
        """
        )
    posturl.short_description = 'post url '
    filter_horizontal = ('categorys',)
    fields = ( 'title','slug','posturl','thubarahalli','meta_description','body','author','status','categorys', )
    readonly_fields = ('posturl',)

    list_display = ('slug','title','status','author',)
    search_fields = ['slug','title',]
    list_filter = ("status",)
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Post,postAdmin)
admin.site.register(category)
admin.site.register(Imagetable)

# Register your models here.
