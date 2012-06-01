# -*- coding: utf-8 -*-
from django import template
from slider.models import SliderImage
import random

register = template.Library()

def get_random_item(l,max=None):
    res= []
    size = len(l)
    indexs = range(0,size)
    if max == None:
        max = size

    for i in range(0, max):
        index = random.choice(indexs)
        indexs.pop(index)
        res += l[index]
    return res

@register.assignment_tag
def get_slider_images(limit=False, randomize=True):
    qs = SliderImage.objects.filter(is_visible=True)
    if randomize is True and limit is True :
        qs = get_random_item(qs,limit)
    elif randomize is True:  
        qs = get_random_item(qs)
    if limit is not False: 
        qs = qs[0:limit]
    return qs
