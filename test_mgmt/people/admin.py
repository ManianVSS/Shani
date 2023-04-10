from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site


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
