from rest_framework import serializers

from .models import Attachment, Tag, FeatureCategory, Feature, UseCase, Requirement


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', ]


class FeatureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureCategory
        fields = ['id', 'name', 'summary', 'description', 'weight', 'parent', 'tags', 'details_file', 'attachments',
                  'org_group', ]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'summary', 'parent', 'description', 'status', 'tags', 'external_id', 'details_file',
                  'attachments', 'org_group', ]


class UseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = ['id', 'name', 'summary', 'description', 'status', 'weight', 'consumer_score', 'serviceability_score',
                  'test_confidence', 'development_confidence', 'feature', 'requirements', 'attachments', 'org_group', ]


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'name', 'summary', 'description', 'use_cases', 'org_group', ]
