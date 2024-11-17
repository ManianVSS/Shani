from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, ProgramIncrement, Epic, Feature, Sprint, Story, Feedback


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', ' file', ]
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(ProgramIncrement)
class ProgramIncrementAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Epic)
class EpicAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        'weight',
        ('pi', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Feature)
class FeatureAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        'weight',
        ('epic', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Sprint)
class SprintAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        'start_date',
        'end_date',
        ('pi', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'start_date', 'end_date', ]


@admin.register(Story)
class StoryAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        'weight',
        'rank',
        ('sprint', RelatedOnlyFieldListFilter),
        ('feature', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Feedback)
class FeedbackAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        'time',
        ('pi', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
