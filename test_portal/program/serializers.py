from api.models import org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import ApplicationType, Application, Release, ArtifactType, Artifact, DocumentType, Document


class ApplicationTypeSerializer(ShaniModelSerializer):
    class Meta:
        model = ApplicationType
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ApplicationSerializer(ShaniModelSerializer):
    class Meta:
        model = Application
        fields = org_model_base_fields + ['application_type', 'name', 'summary', 'description', ]


class ProgramReleaseSerializer(ShaniModelSerializer):
    class Meta:
        model = Release
        fields = org_model_base_fields + ['application', 'name', 'version', 'date', 'summary', 'description',
                                          'release_notes', ]


class ArtifactTypeSerializer(ShaniModelSerializer):
    class Meta:
        model = ArtifactType
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ArtifactSerializer(ShaniModelSerializer):
    class Meta:
        model = Artifact
        fields = org_model_base_fields + ['release', 'artifact_type', 'name', 'link', 'file', 'checksum', ]


class DocumentTypeSerializer(ShaniModelSerializer):
    class Meta:
        model = DocumentType
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class DocumentSerializer(ShaniModelSerializer):
    class Meta:
        model = Document
        fields = org_model_base_fields + ['release', 'document_type', 'name', 'link', 'file', 'checksum', ]


serializer_map = {
    ApplicationType: ApplicationTypeSerializer,
    Application: ApplicationSerializer,
    Release: ProgramReleaseSerializer,
    ArtifactType: ApplicationTypeSerializer,
    Artifact: ArtifactSerializer,
    DocumentType: DocumentTypeSerializer,
    Document: DocumentSerializer,
}
