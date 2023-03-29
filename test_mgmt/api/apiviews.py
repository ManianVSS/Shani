from datetime import datetime, timedelta

import numpy
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UseCase, TestCase, Feature, ExecutionRecord, ReviewStatus, ExecutionRecordStatus, UseCaseCategory, \
    OrgGroup, Engineer, \
    SiteHoliday, Leave, EngineerOrgGroupParticipation
from .serializers import SiteHolidaySerializer, LeaveSerializer

WORK_DAYS_MASK = [1, 1, 1, 1, 1, 0, 0]


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
