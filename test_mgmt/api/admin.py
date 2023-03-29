from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from django.core.exceptions import FieldDoesNotExist
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from massadmin.massadmin import MassEditMixin

from api.models import UseCase, Requirement, ExecutionRecord, Run, Feature, Attachment, Defect, Release, \
    Epic, Sprint, Story, UseCaseCategory, ReliabilityRun, OrgGroup, Engineer, SiteHoliday, Leave, \
    EngineerOrgGroupParticipation, Environment, Topic, TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, \
    Site, Tag, Feedback


class CustomModelAdmin(MassEditMixin, ImportExportModelAdmin):
    save_as = True

    # search_fields = ['name', 'summary', 'description', ]

    def has_view_permission(self, request, obj=None):
        if (request is None) or (request.user is None):
            return False
        if request.user.is_superuser:
            return True
        if obj is None:
            return True
        if super().has_view_permission(request, obj):
            return True

        try:
            return obj.is_owner(request.user) or obj.is_member(request.user)
        except FieldDoesNotExist:
            return False

    def has_change_permission(self, request, obj=None):
        if (request is None) or (request.user is None):
            return False
        if request.user.is_superuser:
            return True
        if obj is None:
            return True
        if super().has_change_permission(request, obj):
            try:
                can_change = obj.is_owner(request.user) or obj.is_member(request.user)
                return can_change
            except FieldDoesNotExist:
                return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if (request is None) or (request.user is None):
            return False
        if request.user.is_superuser:
            return True
        if obj is None:
            return True
        if super().has_delete_permission(request, obj):
            try:
                can_delete = obj.is_owner(request.user)
                return can_delete
            except FieldDoesNotExist:
                return True
        else:
            return False


class AttachmentResource(resources.ModelResource):
    class Meta:
        model = Attachment


class AttachmentAdmin(CustomModelAdmin):
    resource_class = AttachmentResource
    search_fields = ['name', ' file', ]


admin.site.register(Attachment, AttachmentAdmin)


class OrgGroupResource(resources.ModelResource):
    class Meta:
        model = OrgGroup


class OrgGroupAdmin(CustomModelAdmin):
    resource_class = OrgGroupResource


admin.site.register(OrgGroup, OrgGroupAdmin)


class SiteResource(resources.ModelResource):
    class Meta:
        model = Site


class SiteAdmin(CustomModelAdmin):
    resource_class = SiteResource


admin.site.register(Site, SiteAdmin)


class EngineerResource(resources.ModelResource):
    class Meta:
        model = Engineer


class EngineerAdmin(CustomModelAdmin):
    resource_class = EngineerResource


admin.site.register(Engineer, EngineerAdmin)


class ReleaseResource(resources.ModelResource):
    class Meta:
        model = Release


class ReleaseAdmin(CustomModelAdmin):
    resource_class = ReleaseResource


admin.site.register(Release, ReleaseAdmin)


class EngineerOrgGroupParticipationResource(resources.ModelResource):
    class Meta:
        model = EngineerOrgGroupParticipation


class EngineerOrgGroupParticipationAdmin(CustomModelAdmin):
    resource_class = EngineerOrgGroupParticipationResource


admin.site.register(EngineerOrgGroupParticipation, EngineerOrgGroupParticipationAdmin)


class SiteHolidayResource(resources.ModelResource):
    class Meta:
        model = SiteHoliday


class SiteHolidayAdmin(CustomModelAdmin):
    resource_class = SiteHolidayResource


admin.site.register(SiteHoliday, SiteHolidayAdmin)


class LeaveResource(resources.ModelResource):
    class Meta:
        model = Leave


class LeaveAdmin(CustomModelAdmin):
    list_filter = (
        ('engineer', RelatedOnlyFieldListFilter),
        'status',
    )
    resource_class = LeaveResource


admin.site.register(Leave, LeaveAdmin)


class EngineerOrgGroupParticipationHistoryResource(resources.ModelResource):
    class Meta:
        model = EngineerOrgGroupParticipationHistory


class EngineerOrgGroupParticipationHistoryAdmin(CustomModelAdmin):
    resource_class = EngineerOrgGroupParticipationHistoryResource


admin.site.register(EngineerOrgGroupParticipationHistory, EngineerOrgGroupParticipationHistoryAdmin)


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


class UseCaseCategoryResource(resources.ModelResource):
    class Meta:
        model = UseCaseCategory


class UseCaseCategoryAdmin(CustomModelAdmin):
    resource_class = UseCaseCategoryResource


admin.site.register(UseCaseCategory, UseCaseCategoryAdmin)


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


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(CustomModelAdmin):
    resource_class = TagResource


admin.site.register(Tag, TagAdmin)


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


class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic


class TopicAdmin(CustomModelAdmin):
    resource_class = TopicResource


admin.site.register(Topic, TopicAdmin)


class TopicEngineerAssignmentResource(resources.ModelResource):
    class Meta:
        model = TopicEngineerAssignment


class TopicEngineerAssignmentAdmin(CustomModelAdmin):
    resource_class = TopicEngineerAssignmentResource


admin.site.register(TopicEngineerAssignment, TopicEngineerAssignmentAdmin)


class FeedbackResource(resources.ModelResource):
    class Meta:
        model = Feedback


class FeedbackAdmin(CustomModelAdmin):
    resource_class = FeedbackResource


admin.site.register(Feedback, FeedbackAdmin)
