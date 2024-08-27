from django.contrib import admin
from .models import *
class cat(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields ={'slug' :('name',)}
admin.site.register(categ,cat)

class pro(admin.ModelAdmin):
    list_display = ['name','img','slug','price','availability','stock','category','date']
    list_editable = ['img']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register( product, pro)