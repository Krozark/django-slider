django-slider
=============

slider module for django

Requirement:
------------

Django 1.3+

Instalation:
------------

Add in your INSTALL_APPS : 'slider'

    Syncdb to creat slider model

exemple:
-------

In your page.html :

    {% load slider_tags %}

    {% get_slider_image as images [limit=False randomize=True slider=1] %}
    {% for image in images %}
    <li><img src="{{MEDIA_URL}}{{image.image }}"></li>
    {% endfor %}

if you want to use use the default javascripte lib (galleria) just copy/past the slider/template/slider/slider.html

