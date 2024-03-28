from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import SiteSettings, DisplayItem, Page, Category, Catalog, Event


@admin.register(DisplayItem)
class DisplayItemAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'link']


@admin.register(Event)
class EventAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'time',
    )
    search_fields = ['name', 'summary', 'description', 'link', 'time']


@admin.register(Page)
class PageAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published',
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
