from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from massadmin.massadmin import MassEditMixin

from .models import SiteSettings, DisplayItem


def reload_admin_site_name(site_name):
    if site_name is None:
        site_name = "Shani"

        # noinspection PyBroadException
        try:
            site_settings_count = SiteSettings.objects.all().count()
            if site_settings_count > 0:
                site_settings = SiteSettings.objects.all()[0]
                site_name = site_settings.name
        except Exception as e:
            print("Defaulting site name Shani as no site_setting data found")

    admin.site.site_header = site_name + " Website Administration"
    admin.site.site_title = site_name + " Website Admin Portal"
    admin.site.index_title = "Welcome to " + site_name + " Website Administration Portal"


# method for updating
@receiver(post_save, sender=SiteSettings, dispatch_uid="update_admin_site_name")
def update_admin_site_name(sender, instance, **kwargs):
    reload_admin_site_name(instance.name)


reload_admin_site_name(None)


class DisplayItemResource(resources.ModelResource):
    class Meta:
        model = DisplayItem


class DisplayItemAdmin(MassEditMixin, ImportExportModelAdmin):
    resource_class = DisplayItemResource
    save_as = True


admin.site.register(DisplayItem, DisplayItemAdmin)


class SiteSettingsResource(resources.ModelResource):
    class Meta:
        model = SiteSettings


class SiteSettingsAdmin(MassEditMixin, ImportExportModelAdmin):
    resource_class = SiteSettingsResource
    save_as = True


admin.site.register(SiteSettings, SiteSettingsAdmin)
