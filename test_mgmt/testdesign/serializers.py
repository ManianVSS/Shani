from rest_framework import serializers

from .models import TestCase, Attachment, TestCaseCategory, Tag


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', ]


class TestCaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCaseCategory
        fields = ['id', 'name', 'summary', 'description', 'weight', 'parent', 'tags', 'details_file', 'attachments',
                  'org_group', ]


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'name', 'summary', 'parent', 'description', 'status', 'type', 'tags', 'external_id',
                  'details_file', 'attachments', ]
