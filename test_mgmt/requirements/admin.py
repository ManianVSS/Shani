from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, FeatureCategory, Feature, UseCaseCategory, UseCase, RequirementCategory, \
    Requirement


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(FeatureCategory)
class FeatureCategoryAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 5


@admin.register(Feature)
class FeatureAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        'status',
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'status', 'external_id', ]
    display_order = 6


@admin.register(UseCaseCategory)
class UseCaseCategoryAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 1


@admin.register(UseCase)
class UseCaseAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        ('feature', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'status', ]
    display_order = 2


@admin.register(RequirementCategory)
class RequirementCategoryAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 3


@admin.register(Requirement)
class RequirementAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        'status',
        ('category', RelatedOnlyFieldListFilter),
        'cost',
    )
    search_fields = ['name', 'summary', 'description', 'status', 'external_id', ]
    display_order = 4
