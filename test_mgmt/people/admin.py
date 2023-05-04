from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from api.views import default_search_fields
from .models import Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, Attachment, Credit, Scale, Reason


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )


@admin.register(Site)
class SiteAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', ]


@admin.register(Engineer)
class EngineerAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'role',
        ('site', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'employee_id', 'role']


@admin.register(EngineerOrgGroupParticipation)
class EngineerOrgGroupParticipationAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'role',
        ('engineer', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'engineer', 'role']


@admin.register(SiteHoliday)
class SiteHolidayAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('site', RelatedOnlyFieldListFilter),
        'date',
    )
    search_fields = ['name', 'summary', 'date']


@admin.register(Leave)
class LeaveAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        'start_date',
        'end_date',
        'status',
        ('engineer', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'engineer', 'summary', 'start_date', 'end_date', ]


@admin.register(EngineerOrgGroupParticipationHistory)
class EngineerOrgGroupParticipationHistoryAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'date',
        ('engineer', RelatedOnlyFieldListFilter),
    )
    search_fields = ['engineer', ]


@admin.register(Topic)
class TopicAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('parent_topic', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description']


@admin.register(TopicEngineerAssignment)
class TopicEngineerAssignmentAdmin(CustomModelAdmin):
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


@admin.register(Scale)
class ScaleAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = default_search_fields


@admin.register(Reason)
class ReasonAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = default_search_fields


@admin.register(Credit)
class CreditAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        'time',
        ('credited_user', RelatedOnlyFieldListFilter),
        ('scale', RelatedOnlyFieldListFilter),
        ('reason', RelatedOnlyFieldListFilter),
        ('creditor', RelatedOnlyFieldListFilter),
    )
    search_fields = ['time', 'description', ]
