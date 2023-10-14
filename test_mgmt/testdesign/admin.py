from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, TestCaseCategory, TestCase


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = (
        'created_at', 'updated_at', 'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(TestCaseCategory)
class TestCaseCategoryAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'tags']


@admin.register(TestCase)
class TestCaseAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
        'status',
        ('tags', RelatedOnlyFieldListFilter),
        ('use_cases', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'status', 'tags', 'external_id', 'use_cases', ]
