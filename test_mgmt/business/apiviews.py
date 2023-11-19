from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import OrgGroup, RequirementCategory, Requirement
from .serializers import RequirementSerializer, TagSerializer, AttachmentSerializer, RequirementCategorySerializer

WORK_DAYS_MASK = [1, 1, 1, 1, 1, 0, 0]


def get_requirements_as_object(requirements):
    return RequirementSerializer(requirements, many=True).data


def get_requirement_category_requirements(org_group, requirement_category):
    try:
        if requirement_category:
            if org_group:
                return Requirement.objects.filter(parent=requirement_category, org_group=org_group)
            else:
                return Requirement.objects.filter(parent=requirement_category, org_group__isnull=True)
        else:
            if org_group:
                return Requirement.objects.filter(parent__isnull=True, org_group=org_group)
            else:
                return Requirement.objects.filter(parent__isnull=True, org_group__isnull=True)
    except Requirement.DoesNotExist:
        return []


def get_requirement_category_sub_requirement_categories(org_group, requirement_category):
    try:
        if requirement_category:
            if org_group:
                return RequirementCategory.objects.filter(parent=requirement_category, org_group=org_group)
            else:
                return RequirementCategory.objects.filter(parent=requirement_category, org_group__isnull=True)
        else:
            if org_group:
                return RequirementCategory.objects.filter(parent__isnull=True, org_group=org_group)
            else:
                return RequirementCategory.objects.filter(parent__isnull=True, org_group__isnull=True)
    except RequirementCategory.DoesNotExist:
        return []


def get_org_group(org_group_id):
    return OrgGroup.objects.get(pk=org_group_id) if org_group_id else None


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def browse_requirements_category(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    org_group_id = None
    # Set requirement category query set to be based on org group or
    if 'org_group' in request.GET:
        org_group_id = request.query_params.get('org_group')
    try:
        org_group = OrgGroup.objects.get(pk=org_group_id) if org_group_id else None
    except OrgGroup.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Could not find org_group passed')

    requirement_category_id = None
    if 'requirement_category_id' in request.GET:
        requirement_category_id = request.query_params.get('requirement_category_id')
    try:
        requirement_category = RequirementCategory.objects.get(
            pk=requirement_category_id) if requirement_category_id else None
    except RequirementCategory.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Could not find requirement category passed')

    catalog_data = {
        'org_group': requirement_category.org_group if requirement_category else None,
        'parent': requirement_category.parent if requirement_category else None,
        'name': requirement_category.name if requirement_category else "/",
        'summary': requirement_category.summary if requirement_category else "/",
        'description': requirement_category.description if requirement_category else "/",
        'tags': TagSerializer(requirement_category.tags, many=True).data if requirement_category else None,
        'details_file': str(requirement_category.details_file.url) if requirement_category else None,
        'attachments': AttachmentSerializer(requirement_category.attachments,
                                            many=True).data if requirement_category else None,
        'sub_categories': RequirementCategorySerializer(
            get_requirement_category_sub_requirement_categories(org_group, requirement_category), many=True).data,
        'requirements': RequirementSerializer(
            get_requirement_category_requirements(org_group, requirement_category), many=True).data
    }

    return Response(catalog_data)
