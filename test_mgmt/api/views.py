from django.contrib.auth.models import User, Group
from django.core.exceptions import FieldDoesNotExist
from rest_framework import viewsets
from rest_framework.permissions import DjangoObjectPermissions, DjangoModelPermissions, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Attachment, OrgGroup, Properties, Configuration
from .serializers import UserSerializer, GroupSerializer, AttachmentSerializer, OrgGroupSerializer, \
    PropertiesSerializer, ConfigurationSerializer

exact_fields_filter_lookups = ['exact', ]
# many_to_many_id_field_lookups = ['contains']
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


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class DjangoObjectPermissionsOrAnonReadOnly(DjangoObjectPermissions):
    """
    Similar to DjangoObjectPermissions, except that anonymous users are
    allowed read-only access.
    """
    authenticated_users_only = False


class ShaniOrgGroupViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if (user is None) or user.is_superuser:
            return super().get_queryset()

        model = self.queryset.model

        if (self.action == 'list') and hasattr(model, 'get_list_query_set'):
            return model.get_list_query_set(model, self.request.user)
        else:
            return super().get_queryset()


class ShaniOrgGroupObjectLevelPermission(DjangoModelPermissions):
    # authenticated_users_only = False

    def has_permission(self, request, view):

        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or request.user.is_anonymous:
            queryset = self._queryset(view)
            return hasattr(queryset.model, 'can_read')
        else:
            return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
        #     return True

        # if not super().has_object_permission(request, view, obj):
        #     return False

        user = request.user
        if (user is None) or user.is_superuser:
            return super().has_object_permission(request, view, obj)

        queryset = self._queryset(view)
        model_cls = queryset.model

        try:
            match request.method:
                case 'HEAD' | 'OPTIONS':
                    return super().has_object_permission(request, view, obj)
                case 'POST':
                    return True
                case 'GET':
                    return not hasattr(model_cls, 'can_read') or model_cls.can_read(obj, request.user)
                case 'PUT' | "PATCH":
                    return not hasattr(model_cls, 'can_modify') or model_cls.can_modify(obj, request.user)
                case 'DELETE':
                    return not hasattr(model_cls, 'can_delete') or model_cls.can_delete(obj, request.user)
                case _:
                    return False
        except FieldDoesNotExist:
            return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]
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
    permission_classes = [IsSuperUser]
    search_fields = ['id', 'name', ]
    ordering_fields = ['id', 'name', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'permissions': id_fields_filter_lookups,
    }


# filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

class ConfigurationViewSet(ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    permission_classes = [IsSuperUser]
    search_fields = ['name', 'value']
    ordering_fields = ['id', 'name', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = ['name', 'updated_at']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'value': string_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
    }


class OrgGroupViewSet(ShaniOrgGroupViewSet):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'auth_group', 'org_group', 'leaders', 'created_at', 'updated_at', 'published',
                       'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'auth_group': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'leaders': exact_fields_filter_lookups,
        'members': exact_fields_filter_lookups,
        'guests': exact_fields_filter_lookups,
        'consumers': exact_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


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
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class PropertiesViewSet(ShaniOrgGroupViewSet):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }
