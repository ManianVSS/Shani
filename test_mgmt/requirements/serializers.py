from api.models import org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, FeatureCategory, Feature, UseCaseCategory, UseCase, RequirementCategory, \
    Requirement


class RequirementsAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class RequirementsTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class RequirementsFeatureCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = FeatureCategory
        fields = org_model_base_fields + ['parent', 'name', 'summary', 'description', 'tags', 'details_file',
                                          'attachments', ]


class RequirementsFeatureSerializer(ShaniModelSerializer):
    class Meta:
        model = Feature
        fields = org_model_base_fields + ['parent', 'name', 'summary', 'description', 'status', 'tags', 'external_id',
                                          'details_file', 'attachments', ]


class UseCaseCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = UseCaseCategory
        fields = org_model_base_fields + ['parent', 'name', 'summary', 'description', 'tags', 'details_file',
                                          'attachments', ]


class UseCaseSerializer(ShaniModelSerializer):
    class Meta:
        model = UseCase
        fields = org_model_base_fields + ['feature', 'name', 'summary', 'description', 'status', 'details_file',
                                          'attachments', ]


class RequirementCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = RequirementCategory
        fields = org_model_base_fields + ['parent', 'name', 'summary', 'description', 'tags', 'details_file',
                                          'attachments', ]


class RequirementSerializer(ShaniModelSerializer):
    class Meta:
        model = Requirement
        fields = org_model_base_fields + ['category', 'parent', 'name', 'summary', 'description', 'status', 'tags',
                                          'external_id', 'details_file', 'attachments', 'cost', 'additional_data', ]


serializer_map = {
    Attachment: RequirementsAttachmentSerializer,
    Tag: RequirementsTagSerializer,
    FeatureCategory: RequirementsFeatureCategorySerializer,
    Feature: RequirementsFeatureSerializer,
    UseCaseCategory: UseCaseCategorySerializer,
    UseCase: UseCaseSerializer,
    RequirementCategory: RequirementCategorySerializer,
    Requirement: RequirementSerializer,
}
