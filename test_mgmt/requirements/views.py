import json
from xml.etree import ElementTree as ET

from ALM import ALM
from api.model_creation import create_requirement_model
from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, \
    ShaniOrgGroupViewSet, datetime_fields_filter_lookups, compare_fields_filter_lookups, enum_fields_filter_lookups, \
    org_model_view_set_filterset_fields, org_model_ordering_fields
from .models import Attachment, Tag, FeatureCategory, Feature, UseCaseCategory, UseCase, RequirementCategory, \
    Requirement
from .serializers import RequirementsAttachmentSerializer, RequirementsTagSerializer, \
    RequirementsFeatureCategorySerializer, RequirementsFeatureSerializer, \
    UseCaseCategorySerializer, UseCaseSerializer, RequirementCategorySerializer, RequirementSerializer


class RequirementsAttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = RequirementsAttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class RequirementsTagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = RequirementsTagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class RequirementsFeatureCategoryViewSet(ShaniOrgGroupViewSet):
    queryset = FeatureCategory.objects.all()
    serializer_class = RequirementsFeatureCategorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['parent', 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'parent': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class RequirementsFeatureViewSet(ShaniOrgGroupViewSet):
    queryset = Feature.objects.all()
    serializer_class = RequirementsFeatureSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'parent', 'status', 'external_id', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class RequirementsUseCaseCategoryViewSet(ShaniOrgGroupViewSet):
    queryset = UseCaseCategory.objects.all()
    serializer_class = UseCaseCategorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['parent', 'name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'parent': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class RequirementsUseCaseViewSet(ShaniOrgGroupViewSet):
    queryset = UseCase.objects.all()
    serializer_class = UseCaseSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'feature', 'status', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,

        'feature': fk_fields_filter_lookups,

    }.update(org_model_view_set_filterset_fields)


class RequirementCategoryViewSet(ShaniOrgGroupViewSet):
    queryset = RequirementCategory.objects.all()
    serializer_class = RequirementCategorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'parent', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class RequirementViewSet(ShaniOrgGroupViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'parent', 'status', 'external_id', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'category': fk_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,
        'cost': compare_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


def get_alm_requirements():
    with open('alm_config.json', 'r') as f:
        alm_data = json.loads(f.read())
    alm = ALM(alm_data['ALM_config'])
    alm.login()
    alm_response = alm.fetch_requirements()

    if alm_response.status_code not in [200, 399]:
        print("Error in Fetching requirements data from ALM\n", alm_response.status_code, alm_response.content)
        return

    root = ET.fromstring(alm_response.content)
    requirement_obj_list = []

    if root.find('Entity').attrib['Type'] != 'requirement':
        print("Error in parsing the response from ALM as the requirement type in not found", str(root))
        return

    for item in root.findall('Entity'):
        requirement_obj = create_requirement_model(item)
        requirement_obj_list.append(requirement_obj)

    print("Successfully Fetched the details from ALM")

    for requirement_obj in requirement_obj_list:
        if not requirement_obj.parent:
            for parent_obj in requirement_obj_list:
                if ((requirement_obj.id != parent_obj.id)
                        and requirement_obj.additional_data['parent-id'] == parent_obj.external_id):
                    requirement_obj.parent = parent_obj
                    requirement_obj.save(force_update=True)
                    break
    print("Successfully linked the Requirement to its Parent")
