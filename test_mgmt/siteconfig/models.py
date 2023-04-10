from django.db import models

from api.models import OrgModel, OrgGroup


class DisplayItem(OrgModel):
    class Meta:
        verbose_name_plural = "display items"

    sort_order = models.IntegerField(default=0)
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='image file')


class Page(OrgModel):
    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home', max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='image file')
    display_items = models.ManyToManyField(DisplayItem, related_name='pages', blank=True)
    iframe_link = models.TextField(null=True, blank=True)


class Category(OrgModel):
    class Meta:
        verbose_name_plural = "categories"

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='siteconfig_categories')

    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home', max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='image file')
    display_items = models.ManyToManyField(DisplayItem, related_name='categories', blank=True)
    pages = models.ManyToManyField(Page, related_name='categories', blank=True)


class Catalog(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='siteconfig_catalogs')

    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home', max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='logo image file')
    image = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='image file')
    display_items = models.ManyToManyField(DisplayItem, related_name='catalogs', blank=True)
    categories = models.ManyToManyField(Category, related_name='catalogs', blank=True)


class SiteSettings(OrgModel):
    class Meta:
        verbose_name_plural = "site settings"

    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home', max_length=256, unique=True)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=300, blank=True)
    logo = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='logo image file')
    image = models.FileField(upload_to='site_config', blank=True, null=True, verbose_name='image file')
    catalogs = models.ManyToManyField(Catalog, related_name='site_settings', blank=True)


def get_default_settings():
    site_settings_count = SiteSettings.objects.all().count()
    if site_settings_count > 0:
        return SiteSettings.objects.filter(published=True).order_by('sort_order')[0]
    return None
