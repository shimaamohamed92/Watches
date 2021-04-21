from django.db import models
from django.utils.translation import ugettext_lazy as _
# from gowatches.users.models import User



class Watches(models.Model):
	name =  models.CharField(max_length=50, default='watch', verbose_name=_("Name"))
	image = models.ImageField(upload_to='watches/', null=True, blank=True, verbose_name=_("Image"))
	model = models.CharField(max_length=15, null=True, blank=True, verbose_name=_("Model Number"))


class Varient(models.Model):
    watch = models.ForeignKey(Watches, default='TX', related_name='varient',on_delete=models.CASCADE, verbose_name=_("Varient"))
    name =  models.CharField(max_length=50, default='varient', verbose_name=_("Name"))
    image = models.ImageField(upload_to='watches/', null=True, blank=True, verbose_name=_("Image"))
    model = models.CharField(max_length=15, null=True, blank=True, verbose_name=_("Varient Number"))
    # waiting_list = models.ManyToManyField(User, related_name="varient_list", blank=True)
