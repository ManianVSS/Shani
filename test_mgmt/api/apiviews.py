# @api_view(['GET'])
# def get_score(request):
#     if not request.method == 'GET':
#         return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     all_use_case_categories = UseCaseCategory.objects.all()
#
#     score = {'use_case_category_scores': [],
#              'cumulative_score': 0,
#              'cumulative_weight': 0,
#              }
#
#     total_weight = 0
#     total_score = 0
#
#     for use_case_category in all_use_case_categories:
#         use_case_category_score = {'name': use_case_category.name,
#                                    'cumulative_score': 0,
#                                    'cumulative_weight': 0,
#                                    'score': 0,
#                                    'weight': use_case_category.weight}
#
#         category_use_cases = UseCase.objects.filter(category_id=use_case_category.id)
#
#         use_case_category_total_weight = 0
#         use_case_category_total_score = 0
#         for use_case in category_use_cases:
#             use_case_category_total_weight += use_case.weight
#             use_case_category_total_score += use_case.weight * use_case.get_score()
#         use_case_category_score['cumulative_weight'] = use_case_category_total_weight
#         use_case_category_score['cumulative_score'] = use_case_category_total_score
#         use_case_category_score['score'] = 0 if use_case_category_total_weight == 0 \
#             else use_case_category_total_score / use_case_category_total_weight
#
#         score['use_case_category_scores'].append(use_case_category_score)
#         total_weight += use_case_category.weight
#         total_score += use_case_category.weight * use_case_category_score['score']
#
#     score['cumulative_score'] = total_score
#     score['cumulative_weight'] = total_weight
#     score['score'] = 0 if total_weight == 0 else total_score / total_weight
#
#     return Response(score)


#
# @api_view(['GET'])
# def get_use_case_category_score(request, pk):
#     if not request.method == 'GET':
#         return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     try:
#         category = UseCaseCategory.objects.get(pk=pk)
#     except Feature.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     category_score = {'name': category.name,
#                       'cumulative_score': 0,
#                       'cumulative_weight': 0,
#                       'score': 0}
#
#     category_use_cases = UseCase.objects.filter(category_id=category.id)
#
#     category_total_weight = 0
#     category_total_score = 0
#     category_score['use_case_scores'] = []
#     for use_case in category_use_cases:
#         use_case_score = {'name': use_case.name, 'weight': use_case.weight, 'score': use_case.get_score()}
#         category_score['use_case_scores'].append(use_case_score)
#         category_total_weight += use_case.weight
#         category_total_score += use_case.weight * use_case_score['score']
#     category_score['cumulative_weight'] = category_total_weight
#     category_score['cumulative_score'] = category_total_score
#     category_score['score'] = 0 if category_total_weight == 0 else category_total_score / category_total_weight
#
#     return Response(category_score)
#
#
# @api_view(['GET'])
# def get_use_case_score(request, pk):
#     if not request.method == 'GET':
#         return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     try:
#         use_case = UseCase.objects.get(pk=pk)
#     except UseCase.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     use_case_score = {'name': use_case.name,
#                       'consumer_score': use_case.consumer_score,
#                       'serviceability_score': use_case.serviceability_score,
#                       'test_confidence': use_case.test_confidence,
#                       'development_confidence': use_case.development_confidence,
#                       'score': use_case.get_score()}
#
#     return Response(use_case_score)


# def get_use_case_obj_completion(use_case):
#     testcases = TestCase.objects.filter(use_case=use_case)  # , status=ReviewStatus.APPROVED
#
#     result = {'total_tests': len(testcases), 'unimplemented': not bool(testcases), 'passed': 0, 'failed': 0,
#               'pending': 0, 'completion': 0}
#
#     for testcase in testcases:
#         last_execution_record = ExecutionRecord.objects.filter(name=testcase.name).order_by('-time')[0]
#
#         if not last_execution_record or (last_execution_record.status == ExecutionRecordStatus.PENDING):
#             result['pending'] += 1
#         elif last_execution_record.status == ExecutionRecordStatus.PASS:
#             result['passed'] += 1
#         else:
#             result['failed'] += 1
#
#     if len(testcases) > 0:
#         result['completion'] = result['passed'] / result['total_tests']
#
#     result['completion'] = round(result['completion'], 2)
#     return result


# @api_view(['GET'])
# def get_use_case_completion(request, pk):
#     if not request.method == 'GET':
#         return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     try:
#         use_case = UseCase.objects.get(pk=pk)
#     except UseCase.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     return Response(get_use_case_obj_completion(use_case))


# def get_use_case_category_obj_completion(use_case_category):
#     use_cases = UseCase.objects.filter(category=use_case_category,
#                                        status=ReviewStatus.APPROVED)  # , status=ReviewStatus.APPROVED
#     result = {'total_tests': 0, 'unimplemented': not bool(use_cases), 'passed': 0, 'failed': 0, 'pending': 0,
#               'completion': 0}
#
#     for use_case in use_cases:
#         use_case_result = get_use_case_obj_completion(use_case)
#         result['total_tests'] += use_case_result['total_tests']
#         result['passed'] += use_case_result['passed']
#         result['failed'] += use_case_result['passed']
#         result['pending'] += use_case_result['passed']
#         result['completion'] += use_case_result['completion']
#     if use_cases:
#         # result['passed'] /= len(use_cases)
#         # result['failed'] /= len(use_cases)
#         # result['pending'] /= len(use_cases)
#         result['completion'] /= len(use_cases)
#     result['completion'] = round(result['completion'], 2)
#     return result


# @api_view(['GET'])
# def get_use_case_category_completion(request, pk):
#     if not request.method == 'GET':
#         return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     try:
#         use_case_category = UseCaseCategory.objects.get(pk=pk)
#     except UseCaseCategory.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     return Response(get_use_case_category_obj_completion(use_case_category))


# @api_view(['GET'])
# def get_overall_completion(request):
#     if not request.method == 'GET':
#         return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     use_case_categories = UseCaseCategory.objects.all()
#     result = {'total_tests': 0, 'passed': 0, 'failed': 0, 'pending': 0, 'completion': 0,
#               'use_case_category_completion': []}
#
#     for use_case_category in use_case_categories:
#         use_case_category_result = get_use_case_category_obj_completion(use_case_category)
#         use_case_category_result['name'] = use_case_category.name
#         result['use_case_category_completion'].append(use_case_category_result)
#         result['total_tests'] += use_case_category_result['total_tests']
#         result['passed'] += use_case_category_result['passed']
#         result['failed'] += use_case_category_result['failed']
#         result['pending'] += use_case_category_result['pending']
#         result['completion'] += use_case_category_result['completion']
#     if use_case_categories:
#         result['completion'] /= len(use_case_categories)
#
#     result['completion'] = round(result['completion'], 2)
#     return Response(result)
#     # return Response(get_use_case_category_completion(use_case_category))
