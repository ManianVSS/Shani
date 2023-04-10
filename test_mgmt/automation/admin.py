from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from import_export import resources

from api.admin import CustomModelAdmin
from .models import Step, Attachment, Tag


class AttachmentResource(resources.ModelResource):
    class Meta:
        model = Attachment


class AttachmentAdmin(CustomModelAdmin):
    resource_class = AttachmentResource
    search_fields = ['name', ' file', ]

    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )


admin.site.register(Attachment, AttachmentAdmin)


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(CustomModelAdmin):
    resource_class = TagResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(Tag, TagAdmin)


class StepResource(resources.ModelResource):
    class Meta:
        model = Step


class StepAdmin(CustomModelAdmin):
    resource_class = StepResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('tags', RelatedOnlyFieldListFilter),
        ('test_design_owner', RelatedOnlyFieldListFilter),
        'test_design_status',
        ('automation_owner', RelatedOnlyFieldListFilter),
        'automation_status',
    )

    search_fields = ['name', 'summary', 'description', 'expected_results', 'automation_code_reference', ]

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['test_design_owner'].initial = request.user
    #     form.base_fields['automation_owner'].initial = request.user
    #     return form


admin.site.register(Step, StepAdmin)

# For django guardian ImportExportMixin, GuardedModelAdmin
# For advanced filters AdminAdvancedFiltersMixin,
# e.g. advanced_filter_fields = ('tags', 'test_design_owner', 'modified_by', 'test_design_status', 'automation_owner',
#                           'automation_status',)
