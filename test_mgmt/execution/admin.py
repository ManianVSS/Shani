from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin, org_model_list_filter_base
from .models import Attachment, Tag, Release, Environment, ReliabilityIncident, ReliabilityRun, ExecutionRecord, Run, \
    Defect, Build, ReliabilityIteration


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = org_model_list_filter_base + (    )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Release)
class ReleaseAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (    )
    search_fields = ['name', 'summary', 'description', 'properties', ]


@admin.register(Build)
class BuildAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        'type',
        'build_time',
    )
    search_fields = ['name', 'summary', 'description', 'properties', ]


@admin.register(Defect)
class DefectAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        ('build', RelatedOnlyFieldListFilter),
    )
    search_fields = ['summary', 'description', 'external_id', ]


@admin.register(Run)
class RunAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        ('build', RelatedOnlyFieldListFilter),
        'build',
        'start_time',
        'end_time',
    )
    search_fields = ['name', 'build', ]


@admin.register(ExecutionRecord)
class ExecutionRecordAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'status',
        ('run', RelatedOnlyFieldListFilter),
        ('defects', RelatedOnlyFieldListFilter),
        'start_time',
        'end_time',
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(ReliabilityRun)
class ReliabilityRunAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'status',
        ('release', RelatedOnlyFieldListFilter),
        ('build', RelatedOnlyFieldListFilter),
        'type',
        'testName',
        'testEnvironmentType',
        'testEnvironmentName',
        'start_time',
        'modified_time',
    )
    search_fields = ['name', 'build', 'testName', 'testEnvironmentName', 'targetIPTE', 'ipte', ]


@admin.register(ReliabilityIteration)
class ReliabilityIterationAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('run', RelatedOnlyFieldListFilter),
        'name',
        'index',
        'status',
        'start_time',
        'end_time',
    )
    search_fields = ['results', ]


@admin.register(ReliabilityIncident)
class ReliabilityIncidentAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        ('build', RelatedOnlyFieldListFilter),
        ('run', RelatedOnlyFieldListFilter),
        ('iteration', RelatedOnlyFieldListFilter),
        ('defect', RelatedOnlyFieldListFilter),
        'triaged',
    )
    search_fields = ['summary', 'description', 'external_id', ]


@admin.register(Environment)
class EnvironmentAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('assigned_to', RelatedOnlyFieldListFilter),
        ('current_release', RelatedOnlyFieldListFilter),
        ('current_build', RelatedOnlyFieldListFilter),
        'type',
        'purpose',
    )
    search_fields = ['name', 'summary', 'description', 'purpose', 'type', ]
