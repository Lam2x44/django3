from django.contrib import admin

# Register your models here.
from .models import Storetype,items,itemsdetails
admin.site.register(Storetype)
admin.site.register(items)
admin.site.register(itemsdetails)