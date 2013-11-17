# -*- encoding: UTF-8 -*-

from django.contrib import admin
from slider.models import *

from slider.utils import AdminThumbnailMixin

class SliderAdmin(admin.ModelAdmin, AdminThumbnailMixin):
    list_display= ('thumbnail','is_visible')
    thumbnail_options = {'size': (100,100), 'crop': True}

admin.site.register(SliderImage,SliderAdmin)
