from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, ResourceType, ResourceSet, ResourceSetComponent, Request, Resource


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'file', ]
    display_order = 1


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 2


@admin.register(ResourceType)
class ResourceTypeAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 3


@admin.register(ResourceSet)
class ResourceSetAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 4


@admin.register(ResourceSetComponent)
class ResourceSetComponentAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('resource_set', RelatedOnlyFieldListFilter),
        ('type', RelatedOnlyFieldListFilter),
    )
    display_order = 5


@admin.register(Request)
class RequestAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('requester', RelatedOnlyFieldListFilter),
        ('resource_set', RelatedOnlyFieldListFilter),
        'priority',
        'start_time',
        'end_time',
        'status',
    )
    search_fields = ['name', 'purpose', ]
    display_order = 6


@admin.register(Resource)
class ResourceAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('type', RelatedOnlyFieldListFilter),
        ('assigned_to', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 7
