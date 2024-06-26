from rest_framework import serializers

from .models import Attachment, Step, Tag, MockAPI, AuthenticatorSecret


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'feature', 'name', 'summary', 'description', 'expected_results', 'eta', 'tags',
                  'test_design_owner', 'test_design_status', 'automation_owner', 'automation_status',
                  'automation_code_reference', 'details_file', 'attachments', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class MockAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = MockAPI
        fields = ['id', 'name', 'summary', 'status', 'content_type', 'body', 'http_method', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class AuthenticatorSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticatorSecret
        fields = ['id', 'user', 'secret', 'issuer', 'url', 'qr_code', 'initialized', 'org_group',
                  'created_at', 'updated_at', 'published', ]
