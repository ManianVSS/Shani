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


admin.site.register(Step, StepAdmin)
