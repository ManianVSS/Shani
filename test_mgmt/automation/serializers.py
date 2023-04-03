from rest_framework import serializers

from automation.models import Attachment, Step


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'published', ]


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'feature', 'name', 'summary', 'description', 'expected_results', 'eta', 'tags',
                  'test_design_owner', 'test_design_status', 'automation_owner', 'automation_status',
                  'automation_code_reference', 'details_file', 'attachments', 'org_group', 'published', ]
