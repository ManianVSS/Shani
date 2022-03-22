from django import forms
from django.contrib import admin
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from api.models import UseCase, Requirement, TestCase, ExecutionRecord, Run, Feature, Attachment, Defect, Release, \
    Epic, Sprint, Story

class ModelAdminExtension(ImportExportModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ModelAdminExtension, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


class AttachmentResource(resources.ModelResource):
    class Meta:
        model = Attachment


class AttachmentAdmin(ModelAdminExtension):
    resource_class = AttachmentResource


admin.site.register(Attachment, AttachmentAdmin)


class ReleaseResource(resources.ModelResource):
    class Meta:
        model = Release


class ReleaseAdmin(ModelAdminExtension):
    resource_class = ReleaseResource


admin.site.register(Release, ReleaseAdmin)


class EpicResource(resources.ModelResource):
    class Meta:
        model = Epic


class EpicAdmin(ModelAdminExtension):
    resource_class = EpicResource


admin.site.register(Epic, EpicAdmin)


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class FeatureAdmin(ModelAdminExtension):
    resource_class = FeatureResource


admin.site.register(Feature, FeatureAdmin)


class SprintResource(resources.ModelResource):
    class Meta:
        model = Sprint


class SprintAdmin(ModelAdminExtension):
    resource_class = SprintResource


admin.site.register(Sprint, SprintAdmin)


class StoryResource(resources.ModelResource):
    class Meta:
        model = Story


class StoryAdmin(ModelAdminExtension):
    resource_class = StoryResource


admin.site.register(Story, StoryAdmin)


class UseCaseResource(resources.ModelResource):
    class Meta:
        model = UseCase


class UseCaseAdmin(ModelAdminExtension):
    resource_class = UseCaseResource


admin.site.register(UseCase, UseCaseAdmin)


class RequirementResource(resources.ModelResource):
    class Meta:
        model = Requirement


class RequirementAdmin(ModelAdminExtension):
    resource_class = RequirementResource


admin.site.register(Requirement, RequirementAdmin)


class TestCaseResource(resources.ModelResource):
    class Meta:
        model = TestCase


class TestCaseAdmin(ModelAdminExtension):
    resource_class = TestCaseResource


admin.site.register(TestCase, TestCaseAdmin)


class DefectResource(resources.ModelResource):
    class Meta:
        model = Defect


class DefectAdmin(ModelAdminExtension):
    resource_class = DefectResource


admin.site.register(Defect, DefectAdmin)


class RunResource(resources.ModelResource):
    class Meta:
        model = Run


class RunAdmin(ModelAdminExtension):
    resource_class = RunResource


admin.site.register(Run, RunAdmin)


class ExecutionRecordResource(resources.ModelResource):
    class Meta:
        model = ExecutionRecord


class ExecutionRecordAdmin(ModelAdminExtension):
    resource_class = ExecutionRecordResource


admin.site.register(ExecutionRecord, ExecutionRecordAdmin)
