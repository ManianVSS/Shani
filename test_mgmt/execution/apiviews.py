from datetime import datetime
from threading import RLock

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.views import ToolIntegrationWritePermission, ToolIntegrationDeletePermission
from execution.models import Release, Build, Run, ReliabilityRun
from execution.serializers import RunSerializer, ReliabilityRunSerializer


def create_release_if_missing(name):
    matched_release = Release.objects.filter(name=name)
    if matched_release:
        matched_release = matched_release.first()
    else:
        matched_release = Release.objects.create(name=name)
    return matched_release


def create_build_if_missing(name, release_name):
    release = None
    if release_name:
        release = create_release_if_missing(release_name)
    matched_build = Build.objects.filter(name=name)
    if matched_build:
        matched_build = matched_build.first()
    else:
        matched_build = Build.objects.create(name=name, release=release)
    return matched_build


def create_run_if_missing(name, build_name, release_name):
    current_time = datetime.now()
    release = None
    if release_name:
        release = create_release_if_missing(release_name)

    build = None
    if build_name:
        build = create_build_if_missing(build_name, release_name)

    matched_run = Run.objects.filter(name=name)
    if matched_run:
        matched_run = matched_run.first()
    else:
        matched_run = Run.objects.create(name=name, release=release, build=build, start_time=current_time)
    return matched_run


run_lock = RLock()


@swagger_auto_schema(
    method='get',
    operation_description="Start a run if not exists",
    manual_parameters=[
        openapi.Parameter('build', openapi.IN_QUERY, description="Build name", type=openapi.TYPE_STRING,
                          required=False),
        openapi.Parameter('release', openapi.IN_QUERY, description="Release name", type=openapi.TYPE_STRING,
                          required=False),
        openapi.Parameter('name', openapi.IN_QUERY, description="Run name", type=openapi.TYPE_STRING,
                          required=True),
    ],
    responses={
        200: RunSerializer(),
        400: 'Run name is mandatory',
        405: 'Method not allowed'
    }
)
@api_view(['GET'])
@permission_classes([ToolIntegrationDeletePermission | ToolIntegrationWritePermission])
def start_run(request):
    if not request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    build_name = request.query_params.get('build') if 'build' in request.GET else None
    release_name = request.query_params.get('release') if 'release' in request.GET else None
    run_name = request.query_params.get('name') if 'name' in request.GET else None

    if not run_name:
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Run name is mandatory')

    with run_lock:
        matched_run = create_run_if_missing(run_name, build_name, release_name)

    return Response(RunSerializer(matched_run).data)


@swagger_auto_schema(
    method='get',
    operation_description="Stop a run if exists",
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description="Run name", type=openapi.TYPE_STRING,
                          required=True),
    ],
    responses={
        200: RunSerializer(),
        400: 'Run name is mandatory',
        405: 'Method not allowed'
    }
)
@api_view(['GET'])
@permission_classes([ToolIntegrationDeletePermission | ToolIntegrationWritePermission])
def stop_run(request):
    current_time = datetime.now()
    if not request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    run_name = request.query_params.get('name') if 'name' in request.GET else None

    if not run_name:
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Run name is mandatory')

    with run_lock:
        matched_run = create_run_if_missing(run_name, None, None)
        matched_run.end_time = current_time
        matched_run.save()

    return Response(RunSerializer(matched_run).data)


# def create_execution_record(name, run_name):
#     current_time = datetime.now()
#     run = None
#     if run_name:
#         run = create_run_if_missing(run_name, None, None)
#
#     return ExecutionRecord.objects.create(run=run, name=name, start_time=current_time)
#
#
# @api_view(['GET'])
# @permission_classes([ToolIntegrationDeletePermission | ToolIntegrationWritePermission])
# def start_execution_record(request):
#     if not request.method == 'GET':
#         return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
#     run_name = request.query_params.get('run_name') if 'name' in request.GET else None
#     name = request.query_params.get('name') if 'name' in request.GET else None
#
#     if not run_name:
#         return HttpResponse(status=status.HTTP_400_BAD_REQUEST,
#                             content='Run name is mandatory')
#
#     matched_execution_record = create_execution_record(name, run_name)
#     return Response(RunSerializer(matched_execution_record).data)


def create_reliability_run_if_missing(name, build_name, release_name):
    current_time = datetime.now()
    release = None

    if release_name:
        release = create_release_if_missing(release_name)

    build = None
    if build_name:
        build = create_build_if_missing(build_name, release_name)

    matched_reliability_run = ReliabilityRun.objects.filter(name=name)
    if matched_reliability_run:
        matched_reliability_run = matched_reliability_run.first()
    else:
        matched_reliability_run = ReliabilityRun.objects.create(name=name, release=release, build=build,
                                                                start_time=current_time, modified_time=current_time)
    return matched_reliability_run


@swagger_auto_schema(
    method='get',
    operation_description="Start a reliability run if not exists",
    manual_parameters=[
        openapi.Parameter('build', openapi.IN_QUERY, description="Build name", type=openapi.TYPE_STRING,
                          required=False),
        openapi.Parameter('release', openapi.IN_QUERY, description="Release name", type=openapi.TYPE_STRING,
                          required=False),
        openapi.Parameter('name', openapi.IN_QUERY, description="Run name", type=openapi.TYPE_STRING,
                          required=True),
    ],
    responses={
        200: ReliabilityRunSerializer(),
        400: 'Run name is mandatory',
        405: 'Method not allowed'
    }
)
@api_view(['GET'])
@permission_classes([ToolIntegrationDeletePermission | ToolIntegrationWritePermission])
def start_reliability_run(request):
    if not request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    build_name = request.query_params.get('build') if 'build' in request.GET else None
    release_name = request.query_params.get('release') if 'release' in request.GET else None
    run_name = request.query_params.get('name') if 'name' in request.GET else None

    if not run_name:
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Run name is mandatory')

    with run_lock:
        matched_reliabiilty_run = create_reliability_run_if_missing(run_name, build_name, release_name)
    return Response(ReliabilityRunSerializer(matched_reliabiilty_run).data)


@swagger_auto_schema(
    method='get',
    operation_description="Stop a reliability run if exists",
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description="Run name", type=openapi.TYPE_STRING,
                          required=True),
    ],
    responses={
        200: ReliabilityRunSerializer(),
        400: 'Run name is mandatory',
        405: 'Method not allowed'
    }
)
@api_view(['GET'])
@permission_classes([ToolIntegrationDeletePermission | ToolIntegrationWritePermission])
def stop_reliability_run(request):
    current_time = datetime.now()
    if not request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    run_name = request.query_params.get('name') if 'name' in request.GET else None

    if not run_name:
        return Response(status=status.HTTP_400_BAD_REQUEST, data='Run name is mandatory')

    with run_lock:
        matched_reliabiilty_run = create_reliability_run_if_missing(run_name, None, None)
        matched_reliabiilty_run.modified_time = current_time
        matched_reliabiilty_run.save()
    return Response(ReliabilityRunSerializer(matched_reliabiilty_run).data)
