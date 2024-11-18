from django.db import models

from api.models import OrgGroup, NotMutablePublishOrgModel
from api.storage import CustomFileSystemStorage


class ApplicationType(NotMutablePublishOrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='program_application_types')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Application(NotMutablePublishOrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='program_applications')
    application_type = models.ForeignKey(ApplicationType, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='applications')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Release(NotMutablePublishOrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='program_releases')
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='releases')
    name = models.CharField(max_length=256, )
    version = models.CharField(max_length=256)
    date = models.DateTimeField()
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    release_notes = models.FileField(storage=CustomFileSystemStorage, upload_to='program', blank=True, null=True,
                                     verbose_name='Release notes file')


class ArtifactType(NotMutablePublishOrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='program_artifact_types')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Artifact(NotMutablePublishOrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='program_artifacts')
    release = models.ForeignKey(Release, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='artifacts')
    artifact_type = models.ForeignKey(ArtifactType, on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='artifacts')
    name = models.CharField(max_length=256)
    link = models.TextField(null=True, blank=True)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='program', blank=True, null=True, )
    checksum = models.TextField(null=True, blank=True)


class DocumentType(NotMutablePublishOrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='program_document_types')
    name = models.CharField(max_length=256, )
    summary = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Document(NotMutablePublishOrgModel):
    org_group = models.ForeignKey(OrgGroup, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name='organization group', related_name='program_documents')
    release = models.ForeignKey(Release, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='documents')
    name = models.CharField(max_length=256)
    link = models.TextField(null=True, blank=True)
    file = models.FileField(storage=CustomFileSystemStorage, upload_to='program', blank=True, null=True, )
    checksum = models.TextField(null=True, blank=True)


model_name_map = {
    'ApplicationType': ApplicationType,
    'Application': Application,
    'Release': Release,
    'ArtifactType': ArtifactType,
    'Artifact': Artifact,
    'DocumentType': DocumentType,
    'Document': Document,
}
