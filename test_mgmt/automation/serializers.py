from rest_framework import serializers

from automation.models import Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'name', 'summary', 'description', 'eta', 'test_design_status', 'automation_status',
                  'attachments', ]
