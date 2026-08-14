# class ModelAdminExtension(ImportExportModelAdmin):
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super(ModelAdminExtension, self).formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'description':
#             formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
#         return formfield
