from rest_framework import permissions

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, exact_fields_filter_lookups, compare_fields_filter_lookups, \
    date_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet, \
    datetime_fields_filter_lookups, enum_fields_filter_lookups, org_model_view_set_filterset_fields, \
    base_model_view_set_filterset_fields, org_model_ordering_fields, base_model_ordering_fields
from .models import Engineer, SiteHoliday, Leave, \
    EngineerOrgGroupParticipation, Topic, TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Attachment, \
    Credit, Scale, Reason, EngineerSkills
from .serializers import EngineerSerializer, \
    SiteHolidaySerializer, \
    LeaveSerializer, EngineerOrgGroupParticipationSerializer, TopicSerializer, TopicEngineerAssignmentSerializer, \
    EngineerOrgGroupParticipationHistorySerializer, PeopleAttachmentSerializer, CreditSerializer, \
    ScaleSerializer, ReasonSerializer, EngineerSkillsSerializer


class PeopleAttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = PeopleAttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class EngineerViewSet(ShaniOrgGroupViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['employee_id', 'name', 'auth_user', 'role', 'site', 'points', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'employee_id': exact_fields_filter_lookups,
        'name': exact_fields_filter_lookups,
        'auth_user': fk_fields_filter_lookups,
        'role': exact_fields_filter_lookups,
        'site': fk_fields_filter_lookups,
        'points': compare_fields_filter_lookups,
        'auth_user__username': exact_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class EngineerOrgGroupParticipationViewSet(ShaniOrgGroupViewSet):
    queryset = EngineerOrgGroupParticipation.objects.all()
    serializer_class = EngineerOrgGroupParticipationSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['engineer', 'role', 'capacity', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'engineer': fk_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'role': string_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }.update(base_model_view_set_filterset_fields)


class SiteHolidayViewSet(ShaniOrgGroupViewSet):
    queryset = SiteHoliday.objects.all()
    serializer_class = SiteHolidaySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'date', 'site', ] + base_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'site': fk_fields_filter_lookups,
    }.update(base_model_view_set_filterset_fields)


class LeaveViewSet(ShaniOrgGroupViewSet):
    queryset = Leave.objects.filter(published=True)
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['engineer', 'start_date', 'end_date', 'status', ] + base_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'engineer': fk_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
    }.update(base_model_view_set_filterset_fields)


class EngineerOrgGroupParticipationHistoryViewSet(ShaniOrgGroupViewSet):
    queryset = EngineerOrgGroupParticipationHistory.objects.filter(published=True)
    serializer_class = EngineerOrgGroupParticipationHistorySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['date', 'engineer', 'expected_capacity', 'capacity', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'date': date_fields_filter_lookups,
        'engineer': fk_fields_filter_lookups,
        'expected_capacity': compare_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class TopicViewSet(ShaniOrgGroupViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'description', 'parent_topic', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'parent_topic': fk_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class TopicEngineerAssignmentViewSet(ShaniOrgGroupViewSet):
    queryset = TopicEngineerAssignment.objects.filter(published=True)
    serializer_class = TopicEngineerAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['topic', 'engineer', 'status', 'rating', 'start_date',
                       'end_date', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'topic': fk_fields_filter_lookups,
        'engineer': fk_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'rating': compare_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ScaleViewSet(ShaniOrgGroupViewSet):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ReasonViewSet(ShaniOrgGroupViewSet):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class CreditViewSet(ShaniOrgGroupViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = ['time', 'credited_user', 'scale', 'reason', 'creditor']
    ordering_fields = ['time', 'credited_user', 'scale', 'reason', 'creditor', ]
    ordering = default_ordering
    filterset_fields = {
        'time': date_fields_filter_lookups,
        'credited_user': fk_fields_filter_lookups,
        'credits': compare_fields_filter_lookups,
        'scale': fk_fields_filter_lookups,
        'reason': fk_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'creditor': fk_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class EngineerSkillsViewSet(ShaniOrgGroupViewSet):
    queryset = EngineerSkills.objects.all()
    serializer_class = EngineerSkillsSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['engineer', 'skill', 'experience', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'engineer': fk_fields_filter_lookups,
        'skill': string_fields_filter_lookups,
        'experience': compare_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)
