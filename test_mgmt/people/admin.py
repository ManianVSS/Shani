from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin, org_model_list_filter_base, base_model_list_filter_base
from api.views import default_search_fields
from .models import Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Attachment, Credit, Scale, Reason, \
    EngineerSkills


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = org_model_list_filter_base + ( )


@admin.register(Engineer)
class EngineerAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'role',
        ('site', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'employee_id', 'role']


@admin.register(EngineerOrgGroupParticipation)
class EngineerOrgGroupParticipationAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'role',
        ('engineer', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'engineer', 'role']


@admin.register(SiteHoliday)
class SiteHolidayAdmin(CustomModelAdmin):
    list_filter = base_model_list_filter_base + (
        ('site', RelatedOnlyFieldListFilter),
        'date',
    )
    search_fields = ['name', 'summary', 'date']


@admin.register(Leave)
class LeaveAdmin(CustomModelAdmin):
    list_filter = base_model_list_filter_base + (
        'start_date',
        'end_date',
        'status',
        ('engineer', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'engineer', 'summary', 'start_date', 'end_date', ]


@admin.register(EngineerOrgGroupParticipationHistory)
class EngineerOrgGroupParticipationHistoryAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'date',
        ('engineer', RelatedOnlyFieldListFilter),
    )
    search_fields = ['engineer', ]


@admin.register(Topic)
class TopicAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('parent_topic', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description']


@admin.register(TopicEngineerAssignment)
class TopicEngineerAssignmentAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
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
    list_filter = org_model_list_filter_base + ( )
    search_fields = default_search_fields


@admin.register(Reason)
class ReasonAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = default_search_fields


@admin.register(Credit)
class CreditAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'time',
        ('credited_user', RelatedOnlyFieldListFilter),
        ('scale', RelatedOnlyFieldListFilter),
        ('reason', RelatedOnlyFieldListFilter),
        ('creditor', RelatedOnlyFieldListFilter),
    )
    search_fields = ['time', 'description', ]


@admin.register(EngineerSkills)
class EngineerSkillsAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        'skill',
        ('engineer', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'skill']
