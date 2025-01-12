from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, FeatureCategory, Feature, UseCaseCategory, UseCase, RequirementCategory, \
    Requirement


class AttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class TagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class FeatureCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = FeatureCategory
        fields = ['id', 'name', 'summary', 'description', 'parent', 'tags', 'details_file', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class FeatureSerializer(ShaniModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'summary', 'parent', 'description', 'status', 'tags', 'external_id', 'details_file',
                  'attachments', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class UseCaseCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = UseCaseCategory
        fields = ['id', 'name', 'summary', 'description', 'parent', 'tags', 'details_file', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class UseCaseSerializer(ShaniModelSerializer):
    class Meta:
        model = UseCase
        fields = ['id', 'name', 'summary', 'description', 'status', 'feature', 'attachments', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class RequirementCategorySerializer(ShaniModelSerializer):
    class Meta:
        model = RequirementCategory
        fields = ['id', 'parent', 'name', 'summary', 'description', 'tags', 'details_file', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class RequirementSerializer(ShaniModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'category', 'name', 'summary', 'description', 'status', 'tags', 'external_id', 'details_file',
                  'attachments', 'cost', 'org_group', 'created_at', 'updated_at',
                  'published', ]


serializer_map = {
    Attachment: AttachmentSerializer,
    Tag: TagSerializer,
    FeatureCategory: FeatureCategorySerializer,
    Feature: FeatureSerializer,
    UseCaseCategory: UseCaseCategorySerializer,
    UseCase: UseCaseSerializer,
    RequirementCategory: RequirementCategorySerializer,
    Requirement: RequirementSerializer,
}
