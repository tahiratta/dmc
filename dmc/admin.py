from django.contrib import admin

# Register your models here.
from .models import Menu_items, Sub_items, Sub_of_sub_items, Slider, Research

admin.site.register(Menu_items)
admin.site.register(Sub_items)
admin.site.register(Sub_of_sub_items)
admin.site.register(Slider)
admin.site.register(Research)
