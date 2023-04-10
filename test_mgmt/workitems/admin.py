from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, Release, Epic, Feature, Sprint, Story, Feedback


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


class ReleaseResource(resources.ModelResource):
    class Meta:
        model = Release


class ReleaseAdmin(CustomModelAdmin):
    resource_class = ReleaseResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Release, ReleaseAdmin)


class EpicResource(resources.ModelResource):
    class Meta:
        model = Epic


class EpicAdmin(CustomModelAdmin):
    resource_class = EpicResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'weight',
        ('release', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Epic, EpicAdmin)


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class FeatureAdmin(CustomModelAdmin):
    resource_class = FeatureResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'weight',
        ('epic', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Feature, FeatureAdmin)


class SprintResource(resources.ModelResource):
    class Meta:
        model = Sprint


class SprintAdmin(CustomModelAdmin):
    resource_class = SprintResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'number',
        'start_date',
        'end_date',
        ('release', RelatedOnlyFieldListFilter),
    )

    search_fields = ['number', 'start_date', 'end_date', ]


admin.site.register(Sprint, SprintAdmin)


class StoryResource(resources.ModelResource):
    class Meta:
        model = Story


class StoryAdmin(CustomModelAdmin):
    resource_class = StoryResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'weight',
        'rank',
        ('sprint', RelatedOnlyFieldListFilter),
        ('feature', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Story, StoryAdmin)


class FeedbackResource(resources.ModelResource):
    class Meta:
        model = Feedback


class FeedbackAdmin(CustomModelAdmin):
    resource_class = FeedbackResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'time',
        ('release', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Feedback, FeedbackAdmin)
