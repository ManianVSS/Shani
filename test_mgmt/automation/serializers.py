from rest_framework import serializers

from .models import Attachment, Step, Tag


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published', ]


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'feature', 'name', 'summary', 'description', 'expected_results', 'eta', 'tags',
                  'test_design_owner', 'test_design_status', 'automation_owner', 'automation_status',
                  'automation_code_reference', 'details_file', 'attachments', 'org_group', 'created_at', 'updated_at',
                  'published', ]
