from api.serializers import ShaniModelSerializer
from .models import ApplicationType, Application, Release, ArtifactType, Artifact, DocumentType, Document


class ApplicationTypeSerializer(ShaniModelSerializer):
    class Meta:
        model = ApplicationType
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ApplicationSerializer(ShaniModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'application_type', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class ProgramReleaseSerializer(ShaniModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'application', 'name', 'version', 'date', 'summary', 'description', 'release_notes',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class ArtifactTypeSerializer(ShaniModelSerializer):
    class Meta:
        model = ArtifactType
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ArtifactSerializer(ShaniModelSerializer):
    class Meta:
        model = Artifact
        fields = ['id', 'release', 'artifact_type', 'name', 'link', 'file', 'checksum',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class DocumentTypeSerializer(ShaniModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class DocumentSerializer(ShaniModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'release', 'document_type', 'name', 'link', 'file', 'checksum',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


serializer_map = {
    ApplicationType: ApplicationTypeSerializer,
    Application: ApplicationSerializer,
    Release: ProgramReleaseSerializer,
    ArtifactType: ApplicationTypeSerializer,
    Artifact: ArtifactSerializer,
    DocumentType: DocumentTypeSerializer,
    Document: DocumentSerializer,
}
