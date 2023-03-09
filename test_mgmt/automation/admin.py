from django.contrib import admin
from import_export import resources

from api.admin import CustomModelAdmin
from automation.models import Step, ProductFeature


# Register your models here.
class ProductFeatureResource(resources.ModelResource):
    class Meta:
        model = ProductFeature


class ProductFeatureAdmin(CustomModelAdmin):
    resource_class = ProductFeatureResource
    # save_as = True
    list_filter = ['org_group', 'tags', 'owner', 'status', 'automation_owner', ]

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(ProductFeature, ProductFeatureAdmin)


class StepResource(resources.ModelResource):
    class Meta:
        model = Step


class StepAdmin(CustomModelAdmin):
    resource_class = StepResource
    # save_as = True
    list_filter = ['org_group', 'tags', 'test_design_owner', 'test_design_status', 'automation_owner',
                   'automation_status', ]

    search_fields = ['name', 'summary', 'description', 'expected_results', 'automation_code_reference', ]


admin.site.register(Step, StepAdmin)

# For django guardian ImportExportMixin, GuardedModelAdmin
# For advanced filters AdminAdvancedFiltersMixin,
# e.g. advanced_filter_fields = ('tags', 'test_design_owner', 'modified_by', 'test_design_status', 'automation_owner',
#                           'automation_status',)
