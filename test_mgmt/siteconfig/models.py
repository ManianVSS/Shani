from django.db import models
from django.utils.translation import gettext_lazy

from api.models import Attachment


# Create your models here.

# Test steps for step repository
class SiteSettings(models.Model):
    class Meta:
        verbose_name_plural = "site settings"

    name = models.CharField(max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return str(self.name)
