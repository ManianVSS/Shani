from rest_framework import serializers

from automation.models import Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'name', 'summary', 'description', 'expected_results', 'eta', 'tags', 'test_design_owner',
                  'modified_by', 'test_design_status', 'automation_owner', 'automation_status',
                  'automation_code_reference', 'attachments', ]
