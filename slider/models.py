from django.db import models
from django.utils.translation import ugettext_lazy as _

class SliderImage(models.Model):
    image = models.ImageField(_("Image"),upload_to="uploads/slider")
    is_visible = models.BooleanField(_("Is Visible"), default=True)

    def __unicode__(self):
        return u"%d" % self.id

    class Meta:
        verbose_name = _("Slider image")
        verbose_name_plural = _("Slider Images")
