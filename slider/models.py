from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete
from slider.utils import file_cleanup

class SliderImage(models.Model):
    image = models.ImageField(_("Image"),upload_to="uploads/slider")
    is_visible = models.BooleanField(_("Is Visible"), default=True)
    slider = models.IntegerField(_('Slider number'),default=1)

    def __unicode__(self):
        return u"%d" % self.id

    class Meta:
        verbose_name = _("Slider image")
        verbose_name_plural = _("Slider Images")
post_delete.connect(file_cleanup, sender=SliderImage, dispatch_uid="SliderImage.file_cleanup")
