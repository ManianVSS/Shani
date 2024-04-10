from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import ApplicationType, Application, Release, ArtifactType, Artifact, DocumentType, Document


@admin.register(ApplicationType)
class ApplicationTypeAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Application)
class ApplicationAdmin(CustomModelAdmin):
    list_filter = (
        ('application_type', RelatedOnlyFieldListFilter),
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Release)
class ReleaseAdmin(CustomModelAdmin):
    list_filter = (
        ('application', RelatedOnlyFieldListFilter),
        'date',
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(ArtifactType)
class ArtifactTypeAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Artifact)
class ArtifactAdmin(CustomModelAdmin):
    list_filter = (
        ('release', RelatedOnlyFieldListFilter),
        ('artifact_type', RelatedOnlyFieldListFilter),
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'link', 'file', ]


@admin.register(DocumentType)
class DocumentTypeAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Document)
class DocumentAdmin(CustomModelAdmin):
    list_filter = (
        ('release', RelatedOnlyFieldListFilter),
        ('document_type', RelatedOnlyFieldListFilter),
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'link', 'file', ]
