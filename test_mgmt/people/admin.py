from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, Attachment


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


class SiteResource(resources.ModelResource):
    class Meta:
        model = Site


class SiteAdmin(CustomModelAdmin):
    resource_class = SiteResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', ]


admin.site.register(Site, SiteAdmin)


class EngineerResource(resources.ModelResource):
    class Meta:
        model = Engineer


class EngineerAdmin(CustomModelAdmin):
    resource_class = EngineerResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'role',
        ('site', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'employee_id', 'role']


admin.site.register(Engineer, EngineerAdmin)


class EngineerOrgGroupParticipationResource(resources.ModelResource):
    class Meta:
        model = EngineerOrgGroupParticipation


class EngineerOrgGroupParticipationAdmin(CustomModelAdmin):
    resource_class = EngineerOrgGroupParticipationResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'role',
        ('engineer', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'engineer', 'role']


admin.site.register(EngineerOrgGroupParticipation, EngineerOrgGroupParticipationAdmin)


class SiteHolidayResource(resources.ModelResource):
    class Meta:
        model = SiteHoliday


class SiteHolidayAdmin(CustomModelAdmin):
    resource_class = SiteHolidayResource
    list_filter = (
        'published',
        ('site', RelatedOnlyFieldListFilter),
        'date',
    )

    search_fields = ['name', 'summary', 'site', ]


admin.site.register(SiteHoliday, SiteHolidayAdmin)


class LeaveResource(resources.ModelResource):
    class Meta:
        model = Leave


class LeaveAdmin(CustomModelAdmin):
    resource_class = LeaveResource
    list_filter = (
        'published',
        'start_date',
        'end_date',
        'status',
        ('engineer', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'engineer', 'summary', 'start_date', 'end_date', ]


admin.site.register(Leave, LeaveAdmin)


class EngineerOrgGroupParticipationHistoryResource(resources.ModelResource):
    class Meta:
        model = EngineerOrgGroupParticipationHistory


class EngineerOrgGroupParticipationHistoryAdmin(CustomModelAdmin):
    resource_class = EngineerOrgGroupParticipationHistoryResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'date',
        ('engineer', RelatedOnlyFieldListFilter),
    )

    search_fields = ['engineer', ]


admin.site.register(EngineerOrgGroupParticipationHistory, EngineerOrgGroupParticipationHistoryAdmin)


class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic


class TopicAdmin(CustomModelAdmin):
    resource_class = TopicResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent_topic', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description']


admin.site.register(Topic, TopicAdmin)


class TopicEngineerAssignmentResource(resources.ModelResource):
    class Meta:
        model = TopicEngineerAssignment


class TopicEngineerAssignmentAdmin(CustomModelAdmin):
    resource_class = TopicEngineerAssignmentResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'status',
        'start_date',
        'end_date',
        ('topic', RelatedOnlyFieldListFilter),
        ('engineer', RelatedOnlyFieldListFilter),
        'rating',
    )

    search_fields = ['status', 'start_date', 'end_date']


admin.site.register(TopicEngineerAssignment, TopicEngineerAssignmentAdmin)
