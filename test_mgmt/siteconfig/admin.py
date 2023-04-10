import sys

from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from import_export import resources

from api.admin import CustomModelAdmin
from .models import SiteSettings, DisplayItem, Page, Category, Catalog, get_default_settings


def reload_admin_site_name(site_name):
    if site_name is None:
        site_name = "Shani"

        # noinspection PyBroadException
        try:
            site_name = get_default_settings().name
        except Exception as e:
            print("Defaulting site name Shani as no site_setting data found")

    admin.site.site_header = site_name + " Website Administration"
    admin.site.site_title = site_name + " Website Admin Portal"
    admin.site.index_title = "Welcome to " + site_name + " Website Administration Portal"


# method for updating
@receiver(post_save, sender=SiteSettings, dispatch_uid="update_admin_site_name")
def update_admin_site_name(sender, instance, **kwargs):
    reload_admin_site_name(instance.name)


if 'runserver' in sys.argv:
    reload_admin_site_name(None)


class DisplayItemResource(resources.ModelResource):
    class Meta:
        model = DisplayItem


class DisplayItemAdmin(CustomModelAdmin):
    resource_class = DisplayItemResource


admin.site.register(DisplayItem, DisplayItemAdmin)


class PageResource(resources.ModelResource):
    class Meta:
        model = Page


class PageAdmin(CustomModelAdmin):
    resource_class = PageResource


admin.site.register(Page, PageAdmin)


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(CustomModelAdmin):
    resource_class = CategoryResource


admin.site.register(Category, CategoryAdmin)


class CatalogResource(resources.ModelResource):
    class Meta:
        model = Catalog


class CatalogAdmin(CustomModelAdmin):
    resource_class = CatalogResource


admin.site.register(Catalog, CatalogAdmin)


class SiteSettingsResource(resources.ModelResource):
    class Meta:
        model = SiteSettings


class SiteSettingsAdmin(CustomModelAdmin):
    resource_class = SiteSettingsResource


admin.site.register(SiteSettings, SiteSettingsAdmin)
