from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, Release, Environment, ReliabilityRun, ExecutionRecord, Run, Defect, Build, \
    ReliabilityIteration


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
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


@admin.register(Release)
class ReleaseAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'properties', ]


@admin.register(Build)
class BuildAdmin(CustomModelAdmin):
    list_filter = (
        ('release', RelatedOnlyFieldListFilter),
        'type',
        'build_time',
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', 'properties', ]


@admin.register(Defect)
class DefectAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        ('release', RelatedOnlyFieldListFilter),
        ('build', RelatedOnlyFieldListFilter),
    )
    search_fields = ['summary', 'description', 'external_id', ]


@admin.register(Run)
class RunAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        ('release', RelatedOnlyFieldListFilter),
        ('build', RelatedOnlyFieldListFilter),
        'build',
        'start_time',
        'end_time',
    )
    search_fields = ['name', 'build', ]


@admin.register(ExecutionRecord)
class ExecutionRecordAdmin(CustomModelAdmin):
    # readonly_fields = ('id', 'start_time', 'end_time',)
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        ('run', RelatedOnlyFieldListFilter),
        ('defects', RelatedOnlyFieldListFilter),
        'start_time',
        'end_time',
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(ReliabilityRun)
class ReliabilityRunAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        ('release', RelatedOnlyFieldListFilter),
        ('build', RelatedOnlyFieldListFilter),
        'type',
        'testName',
        'testEnvironmentType',
        'testEnvironmentName',
        ('incidents', RelatedOnlyFieldListFilter),
        'start_time',
        'modified_time',
    )
    search_fields = ['name', 'build', 'testName', 'testEnvironmentName', 'targetIPTE', 'ipte', ]


@admin.register(ReliabilityIteration)
class ReliabilityIterationAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('run', RelatedOnlyFieldListFilter),
        'status',
        'start_time',
        'end_time',
        ('incidents', RelatedOnlyFieldListFilter),
    )
    search_fields = ['results', ]


@admin.register(Environment)
class EnvironmentAdmin(CustomModelAdmin):
    list_filter = (
        ('assigned_to', RelatedOnlyFieldListFilter),
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('current_release', RelatedOnlyFieldListFilter),
        ('current_build', RelatedOnlyFieldListFilter),
        'type',
        'purpose',
    )
    search_fields = ['name', 'summary', 'description', 'purpose', 'type', ]
