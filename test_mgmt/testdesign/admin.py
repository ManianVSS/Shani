from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin, org_model_list_filter_base
from .models import Attachment, Tag, TestCaseCategory, TestCase


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = org_model_list_filter_base + ( )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(TestCaseCategory)
class TestCaseCategoryAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('parent', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'tags']


@admin.register(TestCase)
class TestCaseAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('parent', RelatedOnlyFieldListFilter),
        'status',
        ('tags', RelatedOnlyFieldListFilter),
        ('use_cases', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'status', 'tags', 'external_id', 'specification', 'use_cases', ]
