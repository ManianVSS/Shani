import sys

from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from import_export.admin import ImportExportModelAdmin

from api.admin import CustomModelAdmin
from .models import SiteSettings, DisplayItem, Page, Category, Catalog, Event, Configuration, \
    get_database_name


@admin.register(Configuration)
class ConfigurationAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'value', ]
    ordering = ('name',)
    list_display = ['name', 'value', ]


# class MyAdminSite(AdminSite):
#     @never_cache
#     def index(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['appname'] = get_database_name()
#         return self.index(request, extra_context)


def reload_admin_site_name(site_name):
    if site_name is None:
        site_name = "Shani Test Management"

        # noinspection PyBroadException
        try:
            site_name = get_database_name()
        except Exception as e:
            print("Defaulting site name Shani as no site_setting data found")

    admin.site.site_header = site_name + " Website Administration"
    admin.site.site_title = site_name + " Website Admin Portal"
    admin.site.index_title = "Welcome to " + site_name + " Website Administration Portal"


# method for updating
@receiver(post_save, sender=Configuration, dispatch_uid="update_admin_site_name")
def update_admin_site_name(sender, instance, **kwargs):
    reload_admin_site_name(instance.name)


if 'runserver' in sys.argv:
    reload_admin_site_name(None)


@admin.register(DisplayItem)
class DisplayItemAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'link']


@admin.register(Event)
class EventAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'time',
    )
    search_fields = ['name', 'summary', 'description', 'link', 'time']


@admin.register(Page)
class PageAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'iframe_link']


@admin.register(Category)
class CategoryAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Catalog)
class CatalogAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(SiteSettings)
class SiteSettingsAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'email', ]
