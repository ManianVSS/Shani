from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, compare_fields_filter_lookups, date_fields_filter_lookups, \
    exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet, \
    datetime_fields_filter_lookups, org_model_view_set_filterset_fields, org_model_ordering_fields
from .models import Attachment, Tag, ProgramIncrement, Epic, Feature, Sprint, Story, Feedback
from .serializers import WorkitemsAttachmentSerializer, WorkitemsTagSerializer, ProgramIncrementSerializer, \
    EpicSerializer, \
    WorkitemsFeatureSerializer, \
    SprintSerializer, StorySerializer, FeedbackSerializer


class WorkItemsAttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = WorkitemsAttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class WorkItemsTagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = WorkitemsTagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ProgramIncrementViewSet(ShaniOrgGroupViewSet):
    queryset = ProgramIncrement.objects.all()
    serializer_class = ProgramIncrementSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class EpicViewSet(ShaniOrgGroupViewSet):
    queryset = Epic.objects.all()
    serializer_class = EpicSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', 'pi', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'pi': fk_fields_filter_lookups,
        'pi__name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class WorkItemsFeatureViewSet(ShaniOrgGroupViewSet):
    queryset = Feature.objects.all()
    serializer_class = WorkitemsFeatureSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', 'epic', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'epic': fk_fields_filter_lookups,
        'epic__name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class SprintViewSet(ShaniOrgGroupViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'pi', 'start_date', 'end_date', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'pi': fk_fields_filter_lookups,
        'pi__name': string_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class StoryViewSet(ShaniOrgGroupViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', 'rank', 'sprint', 'feature', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'rank': compare_fields_filter_lookups,
        'sprint': fk_fields_filter_lookups,
        'sprint__name': string_fields_filter_lookups,
        'feature': fk_fields_filter_lookups,
        'feature__name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class FeedbackViewSet(ShaniOrgGroupViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'description', 'pi', ]
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'pi': fk_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)
