import json
from xml.etree import ElementTree as ET

from ALM import ALM
from api.model_creation import create_requirement_model
from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, \
    ShaniOrgGroupViewSet, datetime_fields_filter_lookups, compare_fields_filter_lookups, enum_fields_filter_lookups
from .models import Attachment, Tag, FeatureCategory, Feature, UseCase, RequirementCategory, Requirement
from .serializers import AttachmentSerializer, TagSerializer, FeatureCategorySerializer, FeatureSerializer, \
    UseCaseSerializer, RequirementCategorySerializer, RequirementSerializer


class AttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class FeatureCategoryViewSet(ShaniOrgGroupViewSet):
    queryset = FeatureCategory.objects.all()
    serializer_class = FeatureCategorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'parent', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published',
                       'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,

    }


class FeatureViewSet(ShaniOrgGroupViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'parent', 'status', 'external_id', 'org_group', 'created_at',
                       'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,

    }


class UseCaseViewSet(ShaniOrgGroupViewSet):
    queryset = UseCase.objects.all()
    serializer_class = UseCaseSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'feature', 'status', 'org_group', 'created_at', 'updated_at',
                       'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,

        'feature': fk_fields_filter_lookups,

        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class RequirementCategoryViewSet(ShaniOrgGroupViewSet):
    queryset = RequirementCategory.objects.all()
    serializer_class = RequirementCategorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'parent', 'org_group', 'created_at', 'updated_at', 'published',
                       'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,

    }


class RequirementViewSet(ShaniOrgGroupViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'parent', 'status', 'external_id', 'org_group', 'created_at',
                       'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'category': fk_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,
        'cost': compare_fields_filter_lookups,
        'org_group': fk_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


def get_alm_requirements():
    with open('alm_config.json', 'r') as f:
        alm_data = json.load(f.read())
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
