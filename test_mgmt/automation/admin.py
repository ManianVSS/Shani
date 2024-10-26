from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin
from .models import Step, Attachment, Tag, Properties, MockAPI, AuthenticatorSecret


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Step)
class StepAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        'status',
    )
    search_fields = ['name', 'summary', 'description', 'automation_code_reference', ]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['test_design_owner'].initial = request.user
    #     form.base_fields['automation_owner'].initial = request.user
    #     return form


@admin.register(Properties)
class PropertiesAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'details', ]


@admin.register(MockAPI)
class MockAPIAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        'http_method',
    )
    search_fields = ['name', 'summary', ]


@admin.register(AuthenticatorSecret)
class AuthenticatorSecretAdmin(CustomModelAdmin):
    list_filter = (
        'created_at', 'updated_at', 'published', 'is_public',
        ('org_group', RelatedOnlyFieldListFilter),
        'issuer',
        'user',
        'initialized',
    )
    search_fields = ['user', 'domain', ]
    readonly_fields = ('initialized',)

# For django guardian ImportExportMixin, GuardedModelAdmin
# For advanced filters AdminAdvancedFiltersMixin,
# e.g. advanced_filter_fields = ('tags', 'test_design_owner', 'modified_by', 'test_design_status', 'automation_owner',
#                           'automation_status',)
