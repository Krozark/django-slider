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
