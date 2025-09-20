import io
import os
import tempfile
import time
import zipfile

import pandas as pd
from django.http import FileResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

import test_mgmt.settings
from test_mgmt.dataload import model_name_map, serializer_map, save_data_to_folder, load_data_from_folder


# noinspection PyTypeChecker
@swagger_auto_schema(
    method='get',
    operation_description="Retrieve details of the currently authenticated user.",
    responses={
        200: openapi.Response(
            description="User details retrieved successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
                    'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email Address'),
                    'is_staff': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Staff'),
                    'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Active'),
                    'date_joined': openapi.Schema(type=openapi.FORMAT_DATETIME, description='Date Joined'),
                    'last_login': openapi.Schema(type=openapi.FORMAT_DATETIME, description='Last Login'),
                    'is_superuser': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Superuser'),
                    'groups': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Group ID'),
                                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Group Name'),
                            }
                        ),
                        description='List of groups the user belongs to'
                    ),
                    'user_permissions': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Permission ID'),
                                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Permission Name'),
                                'codename': openapi.Schema(type=openapi.TYPE_STRING, description='Permission Codename'),
                            }
                        ),
                        description='List of user permissions'
                    ),
                }
            )
        ),
        401: "Authentication Required",
        405: "Method Not Allowed"
    }
)
@api_view(['GET'])
def get_user_profile_details(request):
    if not request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not request.user or not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    user = request.user
    user_details = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
        'is_superuser': user.is_superuser,
        'groups': [{'id': group.id, 'name': group.name} for group in user.groups.all()],
        'user_permissions': [{'id': perm.id, 'name': perm.name, 'codename': perm.codename} for perm in
                             user.user_permissions.all()],
    }

    return Response(user_details)


class ExportZIPDataView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_description="Export all application data as a ZIP file. Only accessible by superusers.",
        responses={
            200: openapi.Response(
                description="Data exported successfully.",
                schema=openapi.Schema(
                    type=openapi.TYPE_FILE,
                    format='binary',
                    description='ZIP file containing exported data'
                )
            ),
            401: "Authentication Required",
            403: "Permission Denied",
            405: "Method Not Allowed"
        }
    )
    def get(self, request, *args, **kwargs):
        if not request.method == 'GET':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if not request.user or not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        if not request.user.is_superuser:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        zip_path = os.path.join(test_mgmt.settings.MEDIA_BASE_NAME, f'exported_data_{int(time.time())}.zip')

        with tempfile.TemporaryDirectory() as temp_dir:
            save_data_to_folder(temp_dir)

            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, temp_dir)
                        zipf.write(file_path, arcname)
        response = FileResponse(open(zip_path, 'rb'), as_attachment=True, filename=os.path.basename(zip_path),
                                content_type='application/zip')
        return response


class ImportZIPDataView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(
        operation_description="Import application data from an uploaded ZIP file. Only accessible by superusers.",
        manual_parameters=[
            openapi.Parameter(
                name='file',
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description='ZIP file containing data to import',
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Data imported successfully.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Import status message')
                    }
                )
            ),
            400: "Bad Request - No file provided",
            401: "Authentication Required",
            403: "Permission Denied",
            405: "Method Not Allowed"
        }
    )
    def post(self, request, *args, **kwargs):
        if not request.method == 'POST':
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if not request.user or not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        if not request.user.is_superuser:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_file = request.FILES['file']

        with tempfile.TemporaryDirectory() as temp_dir:
            zip_path = os.path.join(temp_dir, 'imported_data.zip')
            with open(zip_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zipf.extractall(temp_dir)

            load_data_from_folder(temp_dir)

        return Response({'status': 'Data imported successfully'})


@swagger_auto_schema(
    method='get',
    operation_description="Export all application data as an Excel file. Only accessible by superusers.",
    responses={
        200: openapi.Response(
            description="Data exported successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_FILE,
                format='binary',
                description='Excel file containing exported data'
            )
        ),
        401: "Authentication Required",
        403: "Permission Denied",
        405: "Method Not Allowed"
    }
)
@api_view(['GET'])
def export_all_data_as_excel(request):
    if not request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not request.user or not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

    if not request.user.is_superuser:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    excel_buffer = io.BytesIO()

    # noinspection PyTypeChecker
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        for app_label, models in model_name_map.items():
            for model_name, model_class in models.items():
                queryset = model_class.objects.all()
                serializer_cls = serializer_map.get(model_class)
                if serializer_cls:
                    serializer = serializer_cls(queryset, many=True, expand_relation_as_object=False)
                    df = pd.DataFrame(serializer.data)
                    if not df.empty:
                        df.to_excel(writer, sheet_name=f"{app_label}_{model_name}"[:31], index=False)

    excel_buffer.seek(0)

    response = FileResponse(excel_buffer, as_attachment=True, filename='exported_data.xlsx',
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    return response

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
