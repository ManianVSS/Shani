from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UseCase, Requirement, TestCase, Feature, Run, ExecutionRecord, Attachment, Defect, Release, Epic, \
    Sprint, Story, ReviewStatus, ExecutionRecordStatus, UseCaseCategory, ReliabilityRun
from .serializers import UserSerializer, GroupSerializer, UseCaseSerializer, RequirementSerializer, \
    TestCaseSerializer, FeatureSerializer, RunSerializer, ExecutionRecordSerializer, AttachmentSerializer, \
    DefectSerializer, ReleaseSerializer, EpicSerializer, SprintSerializer, StorySerializer, UseCaseCategorySerializer, \
    ReliabilityRunSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


boolean_fields_filter_lookups = ['exact']
id_fields_filter_lookups = ['exact', 'in']
string_fields_filter_lookups = ['exact', 'startswith', 'contains', 'endswith', 'iexact', 'istartswith', 'icontains',
                                'iendswith']
compare_fields_filter_lookups = ['exact', 'lte', 'lt', 'gt', 'gte']
default_search_fields = ['name', 'summary', 'description']
default_ordering = ['id']


# filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name']
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary']
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }


class EpicViewSet(viewsets.ModelViewSet):
    queryset = Epic.objects.all()
    serializer_class = EpicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'release']
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'release__id': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
    }


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'epic']
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'epic__id': id_fields_filter_lookups,
        'epic__name': string_fields_filter_lookups,
    }


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'number', 'release', 'start_date', 'end_date']
    ordering = default_ordering
    filterset_fields = {
        'number': string_fields_filter_lookups,
        'release__id': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'start_date': compare_fields_filter_lookups,
        'end_date': compare_fields_filter_lookups,
    }


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'rank', 'sprint', 'feature']
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'rank': compare_fields_filter_lookups,
        'sprint__id': id_fields_filter_lookups,
        'sprint__number': compare_fields_filter_lookups,
        'feature__id': id_fields_filter_lookups,
        'feature__name': string_fields_filter_lookups,
    }


class UseCaseCategoryViewSet(viewsets.ModelViewSet):
    queryset = UseCaseCategory.objects.all()
    serializer_class = UseCaseCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', ]
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
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
    }


# class StepViewSet(viewsets.ModelViewSet):
#     queryset = Step.objects.all()
#     serializer_class = StepSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     search_fields = default_search_fields
#     ordering_fields = ['id', 'summary', 'actor', 'interface', 'action']
#     ordering = default_ordering
#     filterset_fields = {
#         'summary': string_fields_filter_lookups,
#
#         'actor': string_fields_filter_lookups,
#         'interface': string_fields_filter_lookups,
#         'action': string_fields_filter_lookups,
#     }


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', ]
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'use_cases__id': id_fields_filter_lookups,
    }


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'use_case', 'requirements', 'status', 'acceptance_test', 'automated']
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'acceptance_test': boolean_fields_filter_lookups,
        'automated': boolean_fields_filter_lookups,
        'use_case__id': id_fields_filter_lookups,
        'requirements__id': id_fields_filter_lookups,
    }


class DefectViewSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'summary', 'description', 'external_id', 'release', ]
    ordering = default_ordering
    filterset_fields = {
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,

        'release__id': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
    }


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'time', ]
    ordering = default_ordering
    filterset_fields = {
        'build': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'time': compare_fields_filter_lookups,
    }


class ExecutionRecordViewSet(viewsets.ModelViewSet):
    queryset = ExecutionRecord.objects.all()
    serializer_class = ExecutionRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'status', 'acceptance_test', 'automated', 'run', 'time', ]
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'acceptance_test': boolean_fields_filter_lookups,
        'automated': boolean_fields_filter_lookups,
        'defects__id': id_fields_filter_lookups,
        'run__id': id_fields_filter_lookups,
        'time': compare_fields_filter_lookups,
        # 'testcase__id': id_fields_filter_lookups,
    }


# TODO
class ReliabilityRunViewSet(viewsets.ModelViewSet):
    queryset = ReliabilityRun.objects.all()
    serializer_class = ReliabilityRunSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                       'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount', 'incidentCount',
                       'targetIPTI', 'ipti']
    ordering = default_ordering
    filterset_fields = {
        'build': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'start_time': compare_fields_filter_lookups,
        'modified_time': compare_fields_filter_lookups,
        'testName': string_fields_filter_lookups,
        'testEnvironmentType': string_fields_filter_lookups,
        'testEnvironmentName': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'targetIPTI': compare_fields_filter_lookups,
        'incidents': id_fields_filter_lookups,
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
        use_case_category_score[
            'score'] = 0 if use_case_category_total_weight == 0 else use_case_category_total_score / use_case_category_total_weight

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
    result = {'total_tests': 0, 'passed': 0, 'failed': 0, 'pending': 0, 'completion': 0}

    for use_case_category in use_case_categories:
        use_case_category_result = get_use_case_category_obj_completion(use_case_category)
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
