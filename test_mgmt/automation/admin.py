from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

from api.admin import CustomModelAdmin, org_model_list_filter_base
from .models import Step, Attachment, Tag, Properties, MockAPI, ApplicationUnderTest, ApplicationPage, Element


@admin.register(Attachment)
class AttachmentAdmin(CustomModelAdmin):
    search_fields = ['name', 'file', ]
    list_filter = org_model_list_filter_base + ( )


@admin.register(Tag)
class TagAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'summary', 'description', ]


@admin.register(Step)
class StepAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( 
        ('tags', RelatedOnlyFieldListFilter),
        'status',
    )
    search_fields = ['name', 'summary', 'description', ]
    display_order = 1

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['test_design_owner'].initial = request.user
    #     form.base_fields['automation_owner'].initial = request.user
    #     return form


@admin.register(Properties)
class PropertiesAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( )
    search_fields = ['name', 'details', ]
    display_order = 2


@admin.register(MockAPI)
class MockAPIAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( 
        'http_method',
    )
    search_fields = ['name', 'summary', ]
    display_order = 3


@admin.register(ApplicationUnderTest)
class ApplicationUnderTestAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( 
        # ('start_page', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'details', ]
    display_order = 4


@admin.register(ApplicationPage)
class ApplicationPageAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( 
        ('application', RelatedOnlyFieldListFilter),
        # ('check_element', RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'details', ]
    display_order = 5


@admin.register(Element)
class ElementAdmin(CustomModelAdmin):
    list_filter = org_model_list_filter_base + ( 
        ('page', RelatedOnlyFieldListFilter),
        ('containing_element', RelatedOnlyFieldListFilter),
        'element_type',
        'locator_type',
    )
    search_fields = ['name', 'details', ]
    display_order = 6
