from django.contrib import admin
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, Release, Environment, ReliabilityRun, ExecutionRecord, Run, Defect


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


class DefectResource(resources.ModelResource):
    class Meta:
        model = Defect


class DefectAdmin(CustomModelAdmin):
    resource_class = DefectResource


admin.site.register(Defect, DefectAdmin)


class RunResource(resources.ModelResource):
    class Meta:
        model = Run


class RunAdmin(CustomModelAdmin):
    resource_class = RunResource


admin.site.register(Run, RunAdmin)


class ExecutionRecordResource(resources.ModelResource):
    class Meta:
        model = ExecutionRecord


class ExecutionRecordAdmin(CustomModelAdmin):
    resource_class = ExecutionRecordResource


admin.site.register(ExecutionRecord, ExecutionRecordAdmin)


class ReliabilityRunResource(resources.ModelResource):
    class Meta:
        model = ReliabilityRun


class ReliabilityRunAdmin(CustomModelAdmin):
    resource_class = ReliabilityRunResource


admin.site.register(ReliabilityRun, ReliabilityRunAdmin)


class EnvironmentResource(resources.ModelResource):
    class Meta:
        model = Environment


class EnvironmentAdmin(CustomModelAdmin):
    resource_class = EnvironmentResource


admin.site.register(Environment, EnvironmentAdmin)
