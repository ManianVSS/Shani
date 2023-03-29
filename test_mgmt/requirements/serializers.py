from rest_framework import serializers

from automation.models import Attachment, Step, ProductFeature


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', ]


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['id', 'org_group', 'name', 'summary', 'description', 'tags', 'owner', 'status', 'automation_owner',
                  'details_file', 'attachments', ]


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'org_group', 'name', 'summary', 'description', 'expected_results', 'eta', 'tags',
                  'test_design_owner', 'test_design_status', 'automation_owner', 'automation_status',
                  'automation_code_reference', 'details_file', 'attachments', ]
