from django.db import models

from api.models import OrgModel


class DisplayItem(OrgModel):
    sort_order = models.IntegerField(default=0)
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='image file')

    def __str__(self):
        return str(self.name)


class Page(OrgModel):
    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home', max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='image file')
    display_items = models.ManyToManyField(DisplayItem, related_name='pages', blank=True)

    def __str__(self):
        return str(self.name)


class SiteSettings(OrgModel):
    class Meta:
        verbose_name_plural = "site settings"

    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home', max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=300, blank=True)
    logo = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='logo image file')
    pages = models.ManyToManyField(Page, related_name='site_settings', blank=True)

    def __str__(self):
        return str(self.name)
