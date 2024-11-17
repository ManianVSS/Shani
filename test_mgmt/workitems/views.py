from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, compare_fields_filter_lookups, date_fields_filter_lookups, \
    exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet, \
    datetime_fields_filter_lookups
from .models import Attachment, Tag, ProgramIncrement, Epic, Feature, Sprint, Story, Feedback
from .serializers import AttachmentSerializer, TagSerializer, ProgramIncrementSerializer, EpicSerializer, \
    FeatureSerializer, \
    SprintSerializer, StorySerializer, FeedbackSerializer


class AttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class ProgramIncrementViewSet(ShaniOrgGroupViewSet):
    queryset = ProgramIncrement.objects.all()
    serializer_class = ProgramIncrementSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class EpicViewSet(ShaniOrgGroupViewSet):
    queryset = Epic.objects.all()
    serializer_class = EpicSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'pi', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'pi': fk_fields_filter_lookups,
        'pi__name': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class FeatureViewSet(ShaniOrgGroupViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'epic', 'org_group', 'created_at', 'updated_at',
                       'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'epic': fk_fields_filter_lookups,
        'epic__name': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class SprintViewSet(ShaniOrgGroupViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'number', 'pi', 'start_date', 'end_date', 'org_group', 'created_at', 'updated_at',
                       'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'number': string_fields_filter_lookups,
        'pi': fk_fields_filter_lookups,
        'pi__name': string_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class StoryViewSet(ShaniOrgGroupViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'rank', 'sprint', 'feature', 'org_group', 'created_at',
                       'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'rank': compare_fields_filter_lookups,
        'sprint': fk_fields_filter_lookups,
        'sprint__number': compare_fields_filter_lookups,
        'feature': fk_fields_filter_lookups,
        'feature__name': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class FeedbackViewSet(ShaniOrgGroupViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'description', 'pi', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'pi': fk_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }
