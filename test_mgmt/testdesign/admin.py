from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Attachment, Tag, TestCaseCategory, TestCase


class AttachmentResource(resources.ModelResource):
    class Meta:
        model = Attachment


class AttachmentAdmin(CustomModelAdmin):
    resource_class = AttachmentResource


admin.site.register(Attachment, AttachmentAdmin)


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(CustomModelAdmin):
    resource_class = TagResource


admin.site.register(Tag, TagAdmin)


class TestCaseCategoryResource(resources.ModelResource):
    class Meta:
        model = TestCaseCategory


class TestCaseCategoryAdmin(CustomModelAdmin):
    resource_class = TestCaseCategoryResource


admin.site.register(TestCaseCategory, TestCaseCategoryAdmin)


class TestCaseResource(resources.ModelResource):
    class Meta:
        model = TestCase


class TestCaseAdmin(CustomModelAdmin):
    resource_class = TestCaseResource
    list_filter = (
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        'status',
    )
    search_fields = ['name', 'summary', 'description', ]


admin.site.register(TestCase, TestCaseAdmin)
