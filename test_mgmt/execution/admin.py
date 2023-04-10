from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, Release, Environment, ReliabilityRun, ExecutionRecord, Run, Defect


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


class DefectResource(resources.ModelResource):
    class Meta:
        model = Defect


class DefectAdmin(CustomModelAdmin):
    resource_class = DefectResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('release', RelatedOnlyFieldListFilter),
    )

    search_fields = ['summary', 'description', 'external_id', ]


admin.site.register(Defect, DefectAdmin)


class RunResource(resources.ModelResource):
    class Meta:
        model = Run


class RunAdmin(CustomModelAdmin):
    resource_class = RunResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('release', RelatedOnlyFieldListFilter),
        'build',
        'time',
    )

    search_fields = ['name', 'build', ]


admin.site.register(Run, RunAdmin)


class ExecutionRecordResource(resources.ModelResource):
    class Meta:
        model = ExecutionRecord


class ExecutionRecordAdmin(CustomModelAdmin):
    resource_class = ExecutionRecordResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        'time',
        'acceptance_test',
        'automated',
        ('run', RelatedOnlyFieldListFilter),
        ('defects', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(ExecutionRecord, ExecutionRecordAdmin)


class ReliabilityRunResource(resources.ModelResource):
    class Meta:
        model = ReliabilityRun


class ReliabilityRunAdmin(CustomModelAdmin):
    resource_class = ReliabilityRunResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        ('release', RelatedOnlyFieldListFilter),
        'build',
        'testName',
        'testEnvironmentType',
        'testEnvironmentName',
        'incidents',
    )

    search_fields = ['name', 'build', 'testName', 'testEnvironmentName', 'targetIPTE', 'ipte', ]


admin.site.register(ReliabilityRun, ReliabilityRunAdmin)


class EnvironmentResource(resources.ModelResource):
    class Meta:
        model = Environment


class EnvironmentAdmin(CustomModelAdmin):
    resource_class = EnvironmentResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('current_release', RelatedOnlyFieldListFilter),
        'type',
        'purpose',
    )

    search_fields = ['name', 'summary', 'description', 'purpose', 'type', ]


admin.site.register(Environment, EnvironmentAdmin)
