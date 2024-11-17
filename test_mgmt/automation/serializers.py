from rest_framework import serializers

from .models import Attachment, Tag, Step, Properties, MockAPI, AuthenticatorSecret


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
        fields = ['id', 'feature', 'name', 'summary', 'description', 'eta', 'tags', 'status', 'details_file',
                  'attachments', 'org_group', 'created_at', 'updated_at', 'published', ]


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ['id', 'name', 'details', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


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


serializer_map = {
    Attachment: AttachmentSerializer,
    Tag: TagSerializer,
    Step: StepSerializer,
    Properties: PropertiesSerializer,
    MockAPI: MockAPISerializer,
    AuthenticatorSecret: AuthenticatorSecretSerializer,
}
