from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Attachment, Tag


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'file', ]


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]
