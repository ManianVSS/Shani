from django.contrib import admin
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, FeatureCategory, Feature


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


admin.site.register(FeatureCategory, FeatureCategoryAdmin)


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class FeatureAdmin(CustomModelAdmin):
    resource_class = FeatureResource


admin.site.register(Feature, FeatureAdmin)
