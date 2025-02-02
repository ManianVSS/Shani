import os
import tempfile
from pathlib import Path

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import OrgModel, OrgGroup
from api.storage import CustomFileSystemStorage


class DisplayItem(OrgModel):
    class Meta:
        verbose_name_plural = "display items"

    sort_order = models.IntegerField(default=0)
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    image = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                             verbose_name='image file')


class Event(OrgModel):
    sort_order = models.IntegerField(default=0)
    name = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    image = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                             verbose_name='image file')
    time = models.DateTimeField()


class Page(OrgModel):
    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home Page', max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                             verbose_name='image file')
    display_items = models.ManyToManyField(DisplayItem, related_name='pages', blank=True)
    iframe_link = models.TextField(null=True, blank=True)
    document_file = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True)
    html_file = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config/converted', blank=True,
                                 null=True, verbose_name="converted html file")


document_formats = ['.doc', '.docx', '.odt', '.csv', '.tsv', '.rtf']


@receiver(post_save, sender=Page, dispatch_uid="update_site_page_document_file")
def update_site_page_document_file(sender, instance: Page, **kwargs):
    if instance:
        if not instance.html_file:
            if instance.document_file:
                file_name = instance.document_file.name
                extention = Path(file_name).suffix.lower()
                # if extenstion=='.html':
                #     pass
                if file_name and (extention in document_formats):
                    with tempfile.TemporaryDirectory() as tmp:
                        input_file_path = instance.document_file.path
                        output_file_path = str(Path(tmp, Path(input_file_path).stem)) + ".html"
                        exit_code = os.system(
                            'pandoc -s -c \"{}\" \"{}\" -o \"{}\" --embed-resources'.format(
                                "resources/custom_pandoc_conversion.css",
                                input_file_path,
                                output_file_path))
                        if exit_code == 0:
                            final_html_file_name = str(Path(input_file_path).stem) + ".html"
                            with open(output_file_path, 'rb') as pandoc_temp_file:
                                instance.html_file.save(final_html_file_name, pandoc_temp_file, save=True)

                elif extention != '.html':
                    # Unknown file format error needed
                    pass


class Category(OrgModel):
    class Meta:
        verbose_name_plural = "categories"

    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='siteconfig_categories')

    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Home', max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                             verbose_name='image file')
    display_items = models.ManyToManyField(DisplayItem, related_name='categories', blank=True)
    pages = models.ManyToManyField(Page, related_name='categories', blank=True)


class Catalog(OrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='siteconfig_catalogs')

    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='Main Catalog', max_length=256)
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                            verbose_name='logo image file')
    image = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                             verbose_name='image file')
    display_items = models.ManyToManyField(DisplayItem, related_name='catalogs', blank=True)
    events = models.ManyToManyField(Event, related_name='catalogs', blank=True)
    categories = models.ManyToManyField(Category, related_name='catalogs', blank=True)


class SiteSettings(OrgModel):
    class Meta:
        verbose_name_plural = "site settings"

    sort_order = models.IntegerField(default=0)
    name = models.CharField(default='default', max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=300, blank=True)
    logo = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                            verbose_name='logo image file')
    image = models.FileField(storage=CustomFileSystemStorage, upload_to='site_config', blank=True, null=True,
                             verbose_name='image file')
    catalogs = models.ManyToManyField(Catalog, related_name='site_settings', blank=True)


def get_default_settings():
    site_settings_count = SiteSettings.objects.all().count()
    if site_settings_count > 0:
        return SiteSettings.objects.filter(published=True).order_by('sort_order')[0]
    return None


model_name_map = {
    'DisplayItem': DisplayItem,
    'Event': Event,
    'Page': Page,
    'Category': Category,
    'Catalog': Catalog,
    'SiteSettings': SiteSettings,
}
