from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, FeatureCategory, Feature, Requirement, UseCase


class AttachmentResource(resources.ModelResource):
    class Meta:
        model = Attachment


class AttachmentAdmin(CustomModelAdmin):
    resource_class = AttachmentResource
    search_fields = ['name', ' file', ]

    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )


admin.site.register(Attachment, AttachmentAdmin)


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(CustomModelAdmin):
    resource_class = TagResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Tag, TagAdmin)


class FeatureCategoryResource(resources.ModelResource):
    class Meta:
        model = FeatureCategory


class FeatureCategoryAdmin(CustomModelAdmin):
    resource_class = FeatureCategoryResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        'weight',
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


admin.site.register(FeatureCategory, FeatureCategoryAdmin)


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class FeatureAdmin(CustomModelAdmin):
    resource_class = FeatureResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        'status',
        ('parent', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'status', 'external_id', ]


admin.site.register(Feature, FeatureAdmin)


class UseCaseResource(resources.ModelResource):
    class Meta:
        model = UseCase


class UseCaseAdmin(CustomModelAdmin):
    resource_class = UseCaseResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        'weight',
        ('feature', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'status', ]


admin.site.register(UseCase, UseCaseAdmin)


class RequirementResource(resources.ModelResource):
    class Meta:
        model = Requirement


class RequirementAdmin(CustomModelAdmin):
    resource_class = RequirementResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('use_cases', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Requirement, RequirementAdmin)
