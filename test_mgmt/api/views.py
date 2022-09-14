from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UseCase, Requirement, TestCase, Feature, Run, ExecutionRecord, Attachment, Defect, Release, Epic, \
    Sprint, Story, ReviewStatus, ExecutionRecordStatus, UseCaseCategory, ReliabilityRun, OrgGroup, Engineer, \
    SiteHoliday, Leave, EngineerOrgGroupParticipation, Environment
from .serializers import UserSerializer, GroupSerializer, UseCaseSerializer, RequirementSerializer, \
    TestCaseSerializer, FeatureSerializer, RunSerializer, ExecutionRecordSerializer, AttachmentSerializer, \
    DefectSerializer, ReleaseSerializer, EpicSerializer, SprintSerializer, StorySerializer, UseCaseCategorySerializer, \
    ReliabilityRunSerializer, OrgGroupSerializer, EngineerSerializer, SiteHolidaySerializer, LeaveSerializer, \
    EngineerOrgGroupParticipationSerializer, EnvironmentSerializer

boolean_fields_filter_lookups = ['exact', ]
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
        'is_staff': boolean_fields_filter_lookups,
        'is_active': boolean_fields_filter_lookups,
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
        'auth_group__id': id_fields_filter_lookups,
        'parent_org_group__id': id_fields_filter_lookups,
        'leader': id_fields_filter_lookups,
        'engineer_participation__id': id_fields_filter_lookups,
    }


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'employee_id', 'auth_user', 'role', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'employee_id': string_fields_filter_lookups,
        'auth_user__id': id_fields_filter_lookups,
        'role': string_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
        'org_group_participation__id': id_fields_filter_lookups,
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
        'org_group__id': id_fields_filter_lookups,
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
        'engineer__id': id_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
        'role': string_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }


class SiteHolidayViewSet(viewsets.ModelViewSet):
    queryset = SiteHoliday.objects.all()
    serializer_class = SiteHolidaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'date', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'engineer__id': id_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
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
        'release__id': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'epic__id': id_fields_filter_lookups,
        'epic__name': string_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'release__id': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'sprint__id': id_fields_filter_lookups,
        'sprint__number': compare_fields_filter_lookups,
        'feature__id': id_fields_filter_lookups,
        'feature__name': string_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'org_group__id': id_fields_filter_lookups,
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
        'requirements__id': id_fields_filter_lookups,
        # 'testcases__id': id_fields_filter_lookups,

        'weight': compare_fields_filter_lookups,
        'consumer_score': compare_fields_filter_lookups,
        'serviceability_score': compare_fields_filter_lookups,
        'test_confidence': compare_fields_filter_lookups,
        'development_confidence': compare_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'use_cases__id': id_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
    }


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'use_case', 'requirements', 'status', 'acceptance_test', 'automated']
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'acceptance_test': boolean_fields_filter_lookups,
        'automated': boolean_fields_filter_lookups,
        'use_case__id': id_fields_filter_lookups,
        'requirements__id': id_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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

        'release__id': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'org_group__id': id_fields_filter_lookups,
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
        'acceptance_test': boolean_fields_filter_lookups,
        'automated': boolean_fields_filter_lookups,
        'defects__id': id_fields_filter_lookups,
        'run__id': id_fields_filter_lookups,
        'time': datetime_fields_filter_lookups,
        # 'testcase__id': id_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
        'org_group__id': id_fields_filter_lookups,
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
        'current_release__id': id_fields_filter_lookups,
        'org_group__id': id_fields_filter_lookups,
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
