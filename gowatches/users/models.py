from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from gowatches.wishlists.models import Varient


class User(AbstractUser):
    """Default user for Gowatches."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    CHOICES = (
        ('employee', 'Employee'),
        ('admin', 'Administration'),
        ('subadmin', 'SubAdmin'),
        ('cust', 'Customer'),
    )
    role = CharField(max_length=100, choices=CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name=_("Phone Number"), blank=True,  null=True)
    national_id = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True,
                                     verbose_name=_("National ID"))
    variant_list = models.ManyToManyField(Varient, related_name="variants", blank=True)


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})



# class Teacher(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name="customer_account"
#     )
#     phone = models.CharField(max_length=15, verbose_name=_("Phone Number"))
#     national_id = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True,
#                                      verbose_name=_("Licence ID"))