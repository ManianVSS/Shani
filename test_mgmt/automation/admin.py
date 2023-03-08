from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from automation.models import Step


# Register your models here.

class StepResource(resources.ModelResource):
    class Meta:
        model = Step


class StepAdmin(ImportExportModelAdmin):
    resource_class = StepResource
    save_as = True
    list_filter = ['tags', 'test_design_owner', 'modified_by', 'test_design_status', 'automation_owner',
                   'automation_status', ]

    search_fields = ['name', 'summary', 'description', 'expected_results', 'test_design_owner',
                     'modified_by', 'automation_owner', 'automation_code_reference', ]

#For advanced filters AdminAdvancedFiltersMixin,
# e.g. advanced_filter_fields = ('tags', 'test_design_owner', 'modified_by', 'test_design_status', 'automation_owner',
#                           'automation_status',)

admin.site.register(Step, StepAdmin)
