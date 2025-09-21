from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin, org_model_list_filter_base
from .models import ApplicationType, Application, Release, ArtifactType, Artifact, DocumentType, Document


@admin.register(ApplicationType)
class ApplicationTypeAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Application)
class ApplicationAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('application_type', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Release)
class ReleaseAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('application', RelatedOnlyFieldListFilter),
        'date',
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(ArtifactType)
class ArtifactTypeAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Artifact)
class ArtifactAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        ('artifact_type', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'link', 'file', ]


@admin.register(DocumentType)
class DocumentTypeAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Document)
class DocumentAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + (
        ('release', RelatedOnlyFieldListFilter),
        ('document_type', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'link', 'file', ]
