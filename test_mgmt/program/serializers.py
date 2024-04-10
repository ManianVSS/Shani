from rest_framework import serializers

from .models import ApplicationType, Application, Release, ArtifactType, Artifact, DocumentType, Document


class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationType
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'application_type', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'application', 'name', 'version', 'date', 'summary', 'description', 'release_notes',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class ArtifactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactType
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['id', 'release', 'artifact_type', 'name', 'link', 'file', 'checksum',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'release', 'document_type', 'name', 'link', 'file', 'checksum',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
