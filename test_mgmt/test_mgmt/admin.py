from django.contrib import admin

admin.site.site_header = "Shani Administration"
admin.site.site_title = "Shani Admin Portal"
admin.site.index_title = "Welcome to Shani Portal"

# class ModelAdminExtension(ImportExportModelAdmin):
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(ModelAdminExtension, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield
