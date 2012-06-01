# -*- coding: utf-8 -*-
from django import template
from slider.models import SliderImage

register = template.Library()

@register.assignment_tag
def get_slider_images(limit=False, randomize=True):
    qs = SliderImage.objects.filter(is_visible=True)
    if randomize is True:  qs = qs.order_by('?')
    if limit is not False: qs = qs[0:limit]
    return qs
