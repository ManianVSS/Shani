from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import DjangoObjectPermissions

from .models import Attachment, OrgGroup
from .serializers import UserSerializer, GroupSerializer, AttachmentSerializer, OrgGroupSerializer

exact_fields_filter_lookups = ['exact', ]
id_fields_filter_lookups = ['exact', 'in', ]
string_fields_filter_lookups = ['exact', 'iexact', 'icontains', 'regex', ]
# 'startswith', 'endswith', 'istartswith','iendswith', 'contains',
compare_fields_filter_lookups = ['exact', 'lte', 'lt', 'gt', 'gte', ]
date_fields_filter_lookups = ['exact', 'lte', 'gte', 'range', ]
# date,year, month, day, week, week_day, iso_week, iso_week_day, quarter
datetime_fields_filter_lookups = ['exact', 'lte', 'gte', 'range', ]
# time, hour, minute, second
default_search_fields = ['name', 'summary', 'description', ]
default_ordering = ['id', ]


class DjangoObjectPermissionsOrAnonReadOnly(DjangoObjectPermissions):
    """
    Similar to DjangoObjectPermissions, except that anonymous users are
    allowed read-only access.
    """
    authenticated_users_only = False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    search_fields = ['id', 'username', 'first_name', 'last_name', 'email']
    ordering_fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'username': string_fields_filter_lookups,
        'first_name': string_fields_filter_lookups,
        'last_name': string_fields_filter_lookups,
        'email': string_fields_filter_lookups,
        'is_staff': exact_fields_filter_lookups,
        'is_active': exact_fields_filter_lookups,
        'date_joined': date_fields_filter_lookups,
    }


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
    search_fields = ['id', 'name', ]
    ordering_fields = ['id', 'name', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'permissions': id_fields_filter_lookups,
    }


# filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

class OrgGroupViewSet(viewsets.ModelViewSet):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer
    permission_classes = [DjangoObjectPermissionsOrAnonReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'auth_group', 'org_group', 'leaders', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'auth_group': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'leaders': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [DjangoObjectPermissionsOrAnonReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }
