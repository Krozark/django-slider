# -*- encoding: UTF-8 -*-

from django.contrib import admin
from slider.models import *

class SliderAdmin(admin.ModelAdmin):
	list_display= ('slider','is_visible')
admin.site.register(SliderImage,SliderAdmin)
