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


admin.site.register(Attachment, AttachmentAdmin)


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(CustomModelAdmin):
    resource_class = TagResource


admin.site.register(Tag, TagAdmin)


class FeatureCategoryResource(resources.ModelResource):
    class Meta:
        model = FeatureCategory


class FeatureCategoryAdmin(CustomModelAdmin):
    resource_class = FeatureCategoryResource
    list_filter = (
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]

admin.site.register(FeatureCategory, FeatureCategoryAdmin)


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class FeatureAdmin(CustomModelAdmin):
    resource_class = FeatureResource
    list_filter = (
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        'status',
    )
    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Feature, FeatureAdmin)


class UseCaseResource(resources.ModelResource):
    class Meta:
        model = UseCase


class UseCaseAdmin(CustomModelAdmin):
    resource_class = UseCaseResource


admin.site.register(UseCase, UseCaseAdmin)


class RequirementResource(resources.ModelResource):
    class Meta:
        model = Requirement


class RequirementAdmin(CustomModelAdmin):
    resource_class = RequirementResource


admin.site.register(Requirement, RequirementAdmin)
