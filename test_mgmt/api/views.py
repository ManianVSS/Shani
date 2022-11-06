import json
from datetime import datetime, timedelta

import numpy
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UseCase, Requirement, TestCase, Feature, Run, ExecutionRecord, Attachment, Defect, Release, Epic, \
    Sprint, Story, ReviewStatus, ExecutionRecordStatus, UseCaseCategory, ReliabilityRun, OrgGroup, Engineer, \
    SiteHoliday, Leave, EngineerOrgGroupParticipation, Environment, Topic, TopicEngineerAssignment, \
    EngineerOrgGroupParticipationHistory, Site, TestCaseCategory, Tag
from .serializers import UserSerializer, GroupSerializer, UseCaseSerializer, RequirementSerializer, \
    TestCaseSerializer, FeatureSerializer, RunSerializer, ExecutionRecordSerializer, AttachmentSerializer, \
    DefectSerializer, ReleaseSerializer, EpicSerializer, SprintSerializer, StorySerializer, UseCaseCategorySerializer, \
    ReliabilityRunSerializer, OrgGroupSerializer, EngineerSerializer, SiteHolidaySerializer, LeaveSerializer, \
    EngineerOrgGroupParticipationSerializer, EnvironmentSerializer, TopicSerializer, TopicEngineerAssignmentSerializer, \
    EngineerOrgGroupParticipationHistorySerializer, SiteSerializer, TestCaseCategorySerializer, TagSerializer

WORK_DAYS_MASK = [1, 1, 1, 1, 1, 0, 0]

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

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name']
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
    }


class OrgGroupViewSet(viewsets.ModelViewSet):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'auth_group', 'parent_org_group', 'leader', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'auth_group': id_fields_filter_lookups,
        'parent_org_group': id_fields_filter_lookups,
        'leader': id_fields_filter_lookups,
        'engineer_participation': id_fields_filter_lookups,
    }


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'site', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'employee_id': exact_fields_filter_lookups,
        'name': exact_fields_filter_lookups,
        'auth_user': id_fields_filter_lookups,
        'role': exact_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'site': id_fields_filter_lookups,
        'auth_user__username': exact_fields_filter_lookups,
    }


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class EngineerOrgGroupParticipationViewSet(viewsets.ModelViewSet):
    queryset = EngineerOrgGroupParticipation.objects.all()
    serializer_class = EngineerOrgGroupParticipationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'org_group', 'role', 'capacity', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'role': string_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }


class SiteHolidayViewSet(viewsets.ModelViewSet):
    queryset = SiteHoliday.objects.all()
    serializer_class = SiteHolidaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'date', 'site', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'site': id_fields_filter_lookups,
    }


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'start_date', 'end_date', 'status', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
    }


class EngineerOrgGroupParticipationHistoryViewSet(viewsets.ModelViewSet):
    queryset = EngineerOrgGroupParticipationHistory.objects.all()
    serializer_class = EngineerOrgGroupParticipationHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'date', 'engineer', 'org_group', 'expected_capacity', 'capacity', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'expected_capacity': compare_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }


class EpicViewSet(viewsets.ModelViewSet):
    queryset = Epic.objects.all()
    serializer_class = EpicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'release', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'release': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'epic', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'epic': id_fields_filter_lookups,
        'epic__name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'number', 'release', 'start_date', 'end_date', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'number': string_fields_filter_lookups,
        'release': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'rank', 'sprint', 'feature', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'rank': compare_fields_filter_lookups,
        'sprint': id_fields_filter_lookups,
        'sprint__number': compare_fields_filter_lookups,
        'feature': id_fields_filter_lookups,
        'feature__name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class UseCaseCategoryViewSet(viewsets.ModelViewSet):
    queryset = UseCaseCategory.objects.all()
    serializer_class = UseCaseCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class UseCaseViewSet(viewsets.ModelViewSet):
    queryset = UseCase.objects.all()
    serializer_class = UseCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'category', 'status', 'weight', 'consumer_score',
                       'serviceability_score', 'test_confidence', 'development_confidence', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,

        'category__name': id_fields_filter_lookups,
        'requirements': id_fields_filter_lookups,
        # 'testcases': id_fields_filter_lookups,

        'weight': compare_fields_filter_lookups,
        'consumer_score': compare_fields_filter_lookups,
        'serviceability_score': compare_fields_filter_lookups,
        'test_confidence': compare_fields_filter_lookups,
        'development_confidence': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'use_cases': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }


class TestCaseCategoryViewSet(viewsets.ModelViewSet):
    queryset = TestCaseCategory.objects.all()
    serializer_class = TestCaseCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'parent', 'owner', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'parent': id_fields_filter_lookups,
        'owner': string_fields_filter_lookups,
    }


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'description', 'implemented', 'automated', 'estimate', 'status',
                       'implementation_reference', 'external_id']
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'implemented': exact_fields_filter_lookups,
        'automated': exact_fields_filter_lookups,
        'estimate': datetime_fields_filter_lookups,
        'implementation_reference': id_fields_filter_lookups,
        'external_id': id_fields_filter_lookups,
        'parent_category': id_fields_filter_lookups,
    }


class DefectViewSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'summary', 'description', 'external_id', 'release', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,

        'release': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'time', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'build': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'time': datetime_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class ExecutionRecordViewSet(viewsets.ModelViewSet):
    queryset = ExecutionRecord.objects.all()
    serializer_class = ExecutionRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'status', 'acceptance_test', 'automated', 'run', 'time', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        # 'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        # 'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'acceptance_test': exact_fields_filter_lookups,
        'automated': exact_fields_filter_lookups,
        'defects': id_fields_filter_lookups,
        'run': id_fields_filter_lookups,
        'time': datetime_fields_filter_lookups,
        # 'testcase': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class ReliabilityRunViewSet(viewsets.ModelViewSet):
    queryset = ReliabilityRun.objects.all()
    serializer_class = ReliabilityRunSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                       'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount', 'incidentCount',
                       'targetIPTE', 'ipte', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'build': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'start_time': datetime_fields_filter_lookups,
        'modified_time': datetime_fields_filter_lookups,
        'testName': string_fields_filter_lookups,
        'testEnvironmentType': string_fields_filter_lookups,
        'testEnvironmentName': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'targetIPTE': compare_fields_filter_lookups,
        'incidents': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'type', 'purpose', 'current_release', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'type': string_fields_filter_lookups,
        'purpose': string_fields_filter_lookups,
        'current_release': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'description', 'parent_topic', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'parent_topic': id_fields_filter_lookups,
    }


class TopicEngineerAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TopicEngineerAssignment.objects.all()
    serializer_class = TopicEngineerAssignmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'topic': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'rating': compare_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
    }


@api_view(['GET'])
def get_score(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    all_use_case_categories = UseCaseCategory.objects.all()

    score = {'use_case_category_scores': [],
             'cumulative_score': 0,
             'cumulative_weight': 0,
             }

    total_weight = 0
    total_score = 0

    for use_case_category in all_use_case_categories:
        use_case_category_score = {'name': use_case_category.name,
                                   'cumulative_score': 0,
                                   'cumulative_weight': 0,
                                   'score': 0,
                                   'weight': use_case_category.weight}

        category_use_cases = UseCase.objects.filter(category_id=use_case_category.id)

        use_case_category_total_weight = 0
        use_case_category_total_score = 0
        for use_case in category_use_cases:
            use_case_category_total_weight += use_case.weight
            use_case_category_total_score += use_case.weight * use_case.get_score()
        use_case_category_score['cumulative_weight'] = use_case_category_total_weight
        use_case_category_score['cumulative_score'] = use_case_category_total_score
        use_case_category_score['score'] = 0 if use_case_category_total_weight == 0 \
            else use_case_category_total_score / use_case_category_total_weight

        score['use_case_category_scores'].append(use_case_category_score)
        total_weight += use_case_category.weight
        total_score += use_case_category.weight * use_case_category_score['score']

    score['cumulative_score'] = total_score
    score['cumulative_weight'] = total_weight
    score['score'] = 0 if total_weight == 0 else total_score / total_weight

    return Response(score)


@api_view(['GET'])
def get_use_case_category_score(request, pk):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        category = UseCaseCategory.objects.get(pk=pk)
    except Feature.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    category_score = {'name': category.name,
                      'cumulative_score': 0,
                      'cumulative_weight': 0,
                      'score': 0}

    category_use_cases = UseCase.objects.filter(category_id=category.id)

    category_total_weight = 0
    category_total_score = 0
    category_score['use_case_scores'] = []
    for use_case in category_use_cases:
        use_case_score = {'name': use_case.name, 'weight': use_case.weight, 'score': use_case.get_score()}
        category_score['use_case_scores'].append(use_case_score)
        category_total_weight += use_case.weight
        category_total_score += use_case.weight * use_case_score['score']
    category_score['cumulative_weight'] = category_total_weight
    category_score['cumulative_score'] = category_total_score
    category_score['score'] = 0 if category_total_weight == 0 else category_total_score / category_total_weight

    return Response(category_score)


@api_view(['GET'])
def get_use_case_score(request, pk):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        use_case = UseCase.objects.get(pk=pk)
    except UseCase.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    use_case_score = {'name': use_case.name,
                      'consumer_score': use_case.consumer_score,
                      'serviceability_score': use_case.serviceability_score,
                      'test_confidence': use_case.test_confidence,
                      'development_confidence': use_case.development_confidence,
                      'score': use_case.get_score()}

    return Response(use_case_score)


def get_use_case_obj_completion(use_case):
    testcases = TestCase.objects.filter(use_case=use_case)  # , status=ReviewStatus.APPROVED

    result = {'total_tests': len(testcases), 'unimplemented': not bool(testcases), 'passed': 0, 'failed': 0,
              'pending': 0, 'completion': 0}

    for testcase in testcases:
        last_execution_record = ExecutionRecord.objects.filter(name=testcase.name).order_by('-time')[0]

        if not last_execution_record or (last_execution_record.status == ExecutionRecordStatus.PENDING):
            result['pending'] += 1
        elif last_execution_record.status == ExecutionRecordStatus.PASS:
            result['passed'] += 1
        else:
            result['failed'] += 1

    if len(testcases) > 0:
        result['completion'] = result['passed'] / result['total_tests']

    result['completion'] = round(result['completion'], 2)
    return result


@api_view(['GET'])
def get_use_case_completion(request, pk):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        use_case = UseCase.objects.get(pk=pk)
    except UseCase.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    return Response(get_use_case_obj_completion(use_case))


def get_use_case_category_obj_completion(use_case_category):
    use_cases = UseCase.objects.filter(category=use_case_category,
                                       status=ReviewStatus.APPROVED)  # , status=ReviewStatus.APPROVED
    result = {'total_tests': 0, 'unimplemented': not bool(use_cases), 'passed': 0, 'failed': 0, 'pending': 0,
              'completion': 0}

    for use_case in use_cases:
        use_case_result = get_use_case_obj_completion(use_case)
        result['total_tests'] += use_case_result['total_tests']
        result['passed'] += use_case_result['passed']
        result['failed'] += use_case_result['passed']
        result['pending'] += use_case_result['passed']
        result['completion'] += use_case_result['completion']
    if use_cases:
        # result['passed'] /= len(use_cases)
        # result['failed'] /= len(use_cases)
        # result['pending'] /= len(use_cases)
        result['completion'] /= len(use_cases)
    result['completion'] = round(result['completion'], 2)
    return result


@api_view(['GET'])
def get_use_case_category_completion(request, pk):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        use_case_category = UseCaseCategory.objects.get(pk=pk)
    except UseCaseCategory.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    return Response(get_use_case_category_obj_completion(use_case_category))


@api_view(['GET'])
def get_overall_completion(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    use_case_categories = UseCaseCategory.objects.all()
    result = {'total_tests': 0, 'passed': 0, 'failed': 0, 'pending': 0, 'completion': 0,
              'use_case_category_completion': []}

    for use_case_category in use_case_categories:
        use_case_category_result = get_use_case_category_obj_completion(use_case_category)
        use_case_category_result['name'] = use_case_category.name
        result['use_case_category_completion'].append(use_case_category_result)
        result['total_tests'] += use_case_category_result['total_tests']
        result['passed'] += use_case_category_result['passed']
        result['failed'] += use_case_category_result['failed']
        result['pending'] += use_case_category_result['pending']
        result['completion'] += use_case_category_result['completion']
    if use_case_categories:
        result['completion'] /= len(use_case_categories)

    result['completion'] = round(result['completion'], 2)
    return Response(result)
    # return Response(get_use_case_category_completion(use_case_category))


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_org_capacity_for_time_range(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not (('org_group' in request.GET) and ('from' in request.GET) and ('to' in request.GET)):
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST,
                            content='One of the parameters (org_group/from/to) missing')

    try:
        org_group = OrgGroup.objects.get(pk=request.query_params.get('org_group'))
    except OrgGroup.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Could not find org_group passed')

    from_date = datetime.strptime(request.query_params.get('from'), '%Y-%m-%d').date()
    to_date = datetime.strptime(request.query_params.get('to'), '%Y-%m-%d').date()

    org_group_participation_qs = EngineerOrgGroupParticipation.objects.filter(org_group=org_group)

    work_days = numpy.busday_count(from_date,
                                   to_date + timedelta(days=1),
                                   weekmask=WORK_DAYS_MASK
                                   )

    total_capacity = 0
    engineer_data = {}
    for org_group_participation in org_group_participation_qs:
        engineer = org_group_participation.engineer
        engineer_leave_plans = Leave.objects.filter(engineer=engineer,
                                                    start_date__gte=from_date, start_date__lte=to_date,
                                                    end_date__gte=from_date, end_date__lte=to_date)
        engineer_site_holidays = SiteHoliday.objects.filter(site=engineer.site,
                                                            date__gte=from_date,
                                                            date__lte=to_date)
        engineer_site_holidays_dates = [item.date for item in engineer_site_holidays]
        leave_count = 0
        for engineer_leave in engineer_leave_plans:
            leave_count = leave_count + numpy.busday_count(engineer_leave.start_date,
                                                           engineer_leave.end_date + timedelta(days=1),
                                                           weekmask=WORK_DAYS_MASK,
                                                           holidays=engineer_site_holidays_dates)
        site_holiday_count = len(engineer_site_holidays_dates)
        available_days = work_days - leave_count - site_holiday_count
        capacity = available_days * org_group_participation.capacity
        total_capacity = total_capacity + capacity
        engineer_data[engineer.employee_id] = {'employee_id': engineer.employee_id,
                                               'name': engineer.auth_user.username,
                                               'leave_plans': LeaveSerializer(engineer_leave_plans, many=True).data,
                                               'site_holidays': SiteHolidaySerializer(engineer_site_holidays,
                                                                                      many=True).data,
                                               'engineer_site_holidays_dates': engineer_site_holidays_dates,
                                               'leave_count': leave_count,
                                               'site_holiday_count': site_holiday_count,
                                               'available_days': available_days,
                                               'participation_capacity': org_group_participation.capacity,
                                               'capacity': capacity,
                                               }

    capacity_data = {
        'work_days': work_days,
        'total_capacity': total_capacity,
        'engineer_data': engineer_data,
    }

    return Response(capacity_data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_engineer_capacity_for_time_range(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not (('engineer' in request.GET) and ('from' in request.GET) and ('to' in request.GET)):
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST,
                            content='One of the parameters (engineer/from/to) missing')

    try:
        engineer = Engineer.objects.get(pk=request.query_params.get('engineer'))
    except Engineer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Could not find engineer passed')

    from_date = datetime.strptime(request.query_params.get('from'), '%Y-%m-%d').date()
    to_date = datetime.strptime(request.query_params.get('to'), '%Y-%m-%d').date()

    org_group_participation_qs = EngineerOrgGroupParticipation.objects.filter(engineer=engineer)

    work_days = numpy.busday_count(from_date,
                                   to_date + timedelta(days=1),
                                   weekmask=WORK_DAYS_MASK
                                   )

    engineer_leave_plans = Leave.objects.filter(engineer=engineer,
                                                start_date__gte=from_date, start_date__lte=to_date,
                                                end_date__gte=from_date, end_date__lte=to_date)
    engineer_site_holidays = SiteHoliday.objects.filter(site=engineer.site,
                                                        date__gte=from_date,
                                                        date__lte=to_date)
    engineer_site_holidays_dates = [item.date for item in engineer_site_holidays]
    leave_count = 0
    for engineer_leave in engineer_leave_plans:
        leave_count = leave_count + numpy.busday_count(engineer_leave.start_date,
                                                       engineer_leave.end_date + timedelta(days=1),
                                                       weekmask=WORK_DAYS_MASK,
                                                       holidays=engineer_site_holidays_dates)
    site_holiday_count = len(engineer_site_holidays_dates)
    available_days = work_days - leave_count - site_holiday_count

    org_capacity_data = {}
    for org_group_participation in org_group_participation_qs:
        org_group = org_group_participation.org_group
        participation_capacity = org_group_participation.capacity
        capacity = participation_capacity * available_days
        org_capacity_data[org_group.name] = {
            'name': org_group.name,
            'participation_capacity': participation_capacity,
            'capacity': capacity,
        }

    capacity_data = {
        'work_days': work_days,
        'employee_id': engineer.employee_id,
        'name': engineer.auth_user.username,
        'leave_plans': LeaveSerializer(engineer_leave_plans, many=True).data,
        'engineer_site_holidays_dates': engineer_site_holidays_dates,
        'leave_count': leave_count,
        'site_holidays': SiteHolidaySerializer(engineer_site_holidays,
                                               many=True).data,
        'site_holiday_count': site_holiday_count,
        'available_days': available_days,
        'org_capacity_data': org_capacity_data,
    }

    return Response(capacity_data)

# class ParseExcel(APIView):
#     def post(self, request, format=None):
#         try:
#             excel_file = request.FILES['files']
#         except MultiValueDictKeyError:
#             return redirect ("/error.html")
# @api_view(['GET'])
# def use_case_count(request):
#     count = UseCase.objects.all().count()
#     return Response(count, status=status.HTTP_200_OK)

#
# @api_view(['GET'])
# def requirement_count(request):
#     count = Requirement.objects.all().count()
#     return Response(count, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def test_case_count(request):
#     count = TestCase.objects.all().count()
#     return Response(count, status=status.HTTP_200_OK)

# class StepViewSet(viewsets.ModelViewSet):
#     queryset = Step.objects.all()
#     serializer_class = StepSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     search_fields = default_search_fields
#     ordering_fields = ['id', 'summary', 'actor', 'interface', 'action']
#     ordering = default_ordering
#     filterset_fields = {
#         'id': id_fields_filter_lookups,
#         'summary': string_fields_filter_lookups,
#
#         'actor': string_fields_filter_lookups,
#         'interface': string_fields_filter_lookups,
#         'action': string_fields_filter_lookups,
#     }
