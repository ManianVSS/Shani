from django.http.response import HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    datetime_fields_filter_lookups, compare_fields_filter_lookups, exact_fields_filter_lookups, \
    ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet
from . import ipte_util
from .models import Attachment, Tag, Release, Environment, ReliabilityRun, Defect, Run, ExecutionRecord, Build
from .serializers import AttachmentSerializer, TagSerializer, ReleaseSerializer, EnvironmentSerializer, \
    ReliabilityRunSerializer, DefectSerializer, RunSerializer, ExecutionRecordSerializer, BuildSerializer


class AttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class ReleaseViewSet(ShaniOrgGroupViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class BuildViewSet(ShaniOrgGroupViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'release', 'name', 'type', 'build_time', 'summary', 'org_group', 'created_at',
                       'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'release': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'type': string_fields_filter_lookups,
        'build_time': datetime_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class DefectViewSet(ShaniOrgGroupViewSet):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'summary', 'description', 'external_id', 'release', 'org_group', 'created_at',
                       'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,

        'release': id_fields_filter_lookups,
        'build': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class RunViewSet(ShaniOrgGroupViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'time', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'start_time': datetime_fields_filter_lookups,
        'end_time': datetime_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'release': id_fields_filter_lookups,
        'build': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class ExecutionRecordViewSet(ShaniOrgGroupViewSet):
    queryset = ExecutionRecord.objects.all()
    serializer_class = ExecutionRecordSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'status', 'run', 'start_time', 'org_group', 'created_at', 'updated_at',
                       'published', ]
    ordering = default_ordering
    filterset_fields = {
        # 'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        # 'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'defects': exact_fields_filter_lookups,
        'run': id_fields_filter_lookups,
        'start_time': datetime_fields_filter_lookups,
        'end_time': datetime_fields_filter_lookups,
        # 'testcase': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class ReliabilityRunViewSet(ShaniOrgGroupViewSet):
    queryset = ReliabilityRun.objects.all()
    serializer_class = ReliabilityRunSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                       'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount', 'incidentCount',
                       'targetIPTE', 'ipte', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'release': id_fields_filter_lookups,
        'build': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'start_time': datetime_fields_filter_lookups,
        'modified_time': datetime_fields_filter_lookups,
        'testName': string_fields_filter_lookups,
        'testEnvironmentType': string_fields_filter_lookups,
        'testEnvironmentName': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'targetIPTE': compare_fields_filter_lookups,
        'incidents': exact_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups, 'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class EnvironmentViewSet(ShaniOrgGroupViewSet):
    queryset = Environment.objects.filter(published=True)
    serializer_class = EnvironmentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'type', 'purpose', 'current_release', 'org_group', 'created_at',
                       'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'type': string_fields_filter_lookups,
        'purpose': string_fields_filter_lookups,
        'current_release': id_fields_filter_lookups,
        'current_build': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups, 'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


@api_view(['GET'])
def get_ipte_for_iterations(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    response = ""
    if 'number_of_iterations' not in request.GET:
        response = response + "Warning: Missing parameter number_of_iterations;"
    if 'number_of_incidents' not in request.GET:
        response = response + "Warning: Missing parameter number_of_incidents;"
    if 'confidence_interval' not in request.GET:
        response = response + "Warning: Missing parameter confidence_interval;"
    number_of_iterations = int(request.GET.get('number_of_iterations', '1000'))
    number_of_incidents = int(request.GET.get('number_of_incidents', '0'))
    confidence_interval = float(request.GET.get('confidence_interval', '0.9'))
    ipte = ipte_util.calculate_ipte(number_of_iterations, number_of_incidents, confidence_interval)

    response = str(ipte) + " is the IPTE for " + str(number_of_iterations) + " iterations with " + str(
        number_of_incidents) + " incidents with confidence interval " + str(confidence_interval) + ";" + response
    return Response(response)


@api_view(['GET'])
# @permission_classes([ShaniOrgGroupObjectLevelPermission])
def get_iterations_for_ipte(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    response = ""
    if 'required_ipte' not in request.GET:
        response = response + "Warning: Missing parameter required_ipte;"
    if 'number_of_incidents' not in request.GET:
        response = response + "Warning: Missing parameter number_of_incidents;"
    if 'confidence_interval' not in request.GET:
        response = response + "Warning: Missing parameter confidence_interval;"
    required_ipte = float(request.GET.get('required_ipte', '1.0'))
    number_of_incidents = int(request.GET.get('number_of_incidents', '0'))
    confidence_interval = float(request.GET.get('confidence_interval', '0.9'))
    number_of_iterations = ipte_util.calculate_iterations_required(required_ipte, number_of_incidents,
                                                                   confidence_interval)
    response = str(number_of_iterations) + " is the number of iterations required for " + str(
        required_ipte) + " ipte with " + str(number_of_incidents) + " incidents with confidence interval " + str(
        confidence_interval) + ";" + response
    return Response(response)
