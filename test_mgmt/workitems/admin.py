from django.contrib import admin
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, Release, Epic, Feature, Sprint, Story, Feedback


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


class ReleaseResource(resources.ModelResource):
    class Meta:
        model = Release


class ReleaseAdmin(CustomModelAdmin):
    resource_class = ReleaseResource


admin.site.register(Release, ReleaseAdmin)


class EpicResource(resources.ModelResource):
    class Meta:
        model = Epic


class EpicAdmin(CustomModelAdmin):
    resource_class = EpicResource


admin.site.register(Epic, EpicAdmin)


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class FeatureAdmin(CustomModelAdmin):
    resource_class = FeatureResource


admin.site.register(Feature, FeatureAdmin)


class SprintResource(resources.ModelResource):
    class Meta:
        model = Sprint


class SprintAdmin(CustomModelAdmin):
    resource_class = SprintResource


admin.site.register(Sprint, SprintAdmin)


class StoryResource(resources.ModelResource):
    class Meta:
        model = Story


class StoryAdmin(CustomModelAdmin):
    resource_class = StoryResource


admin.site.register(Story, StoryAdmin)


class FeedbackResource(resources.ModelResource):
    class Meta:
        model = Feedback


class FeedbackAdmin(CustomModelAdmin):
    resource_class = FeedbackResource


admin.site.register(Feedback, FeedbackAdmin)
