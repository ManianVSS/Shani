from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin, org_model_list_filter_base
from .models import Attachment, Tag, FeatureCategory, Feature, UseCaseCategory, UseCase, RequirementCategory, \
    Requirement


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = org_model_list_filter_base + ( )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(FeatureCategory)
class FeatureCategoryAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('tags', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 5


@admin.register(Feature)
class FeatureAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('tags', RelatedOnlyFieldListFilter),
        'status',
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'status', 'external_id', ]
    display_order = 6


@admin.register(UseCaseCategory)
class UseCaseCategoryAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('tags', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 1


@admin.register(UseCase)
class UseCaseAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'status',
        ('feature', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'status', ]
    display_order = 2


@admin.register(RequirementCategory)
class RequirementCategoryAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('tags', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 3


@admin.register(Requirement)
class RequirementAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('tags', RelatedOnlyFieldListFilter),
        'status',
        ('category', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
        'cost',
    )
    search_fields = ['name', 'summary', 'description', 'status', 'external_id', ]
    display_order = 4
