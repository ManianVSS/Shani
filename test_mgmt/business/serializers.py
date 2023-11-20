from rest_framework import serializers

from .models import Attachment, Tag, RequirementCategory, Requirement


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published', ]


class RequirementCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementCategory
        fields = ['id', 'parent', 'name', 'summary', 'description', 'tags', 'details_file', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', ]


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'parent', 'name', 'summary', 'description', 'status', 'tags', 'external_id', 'details_file',
                  'attachments', 'cost', 'org_group', 'created_at', 'updated_at', 'published', ]
