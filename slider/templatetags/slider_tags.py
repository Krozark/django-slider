# -*- coding: utf-8 -*-
from django import template
from slider.models import SliderImage
register = template.Library()

@register.assignment_tag
def get_slider_images(limit=False, randomize=True, slider=1):

    qs = SliderImage.objects.filter(is_visible=True,slider=slider)
    
    if randomize:
        qs = qs.order_by('?')

    if limit:
        qs = qs[0:limit]
    
    return qs
