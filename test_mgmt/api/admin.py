from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from django.core.exceptions import FieldDoesNotExist
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from massadmin.massadmin import MassEditMixin

from api.models import Attachment, OrgGroup, Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, Tag


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


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(CustomModelAdmin):
    resource_class = TagResource


admin.site.register(Tag, TagAdmin)


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
