from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.core.exceptions import FieldDoesNotExist
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from massadmin.massadmin import MassEditMixin

from .models import Attachment, OrgGroup


class CustomModelAdmin(MassEditMixin, ImportExportModelAdmin):
    save_as = True

    # search_fields = ['name', 'summary', 'description', ]

    def has_view_permission(self, request, obj=None):
        if (request is None) or (request.user is None):
            return False
        if request.user.is_superuser:
            return True
        if obj is None:
            return True
        if super().has_view_permission(request, obj):
            try:
                return obj.can_read(request.user)
            except FieldDoesNotExist:
                return False
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if (request is None) or (request.user is None):
            return False
        if request.user.is_superuser:
            return True
        if obj is None:
            return True
        if super().has_change_permission(request, obj):
            try:
                return obj.can_modify(request.user)
            except FieldDoesNotExist:
                return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if (request is None) or (request.user is None):
            return False
        if request.user.is_superuser:
            return True
        if obj is None:
            return True
        if super().has_delete_permission(request, obj):
            try:
                return obj.can_delete(request.user)
            except FieldDoesNotExist:
                return True
        else:
            return False


class CustomUserAdmin(CustomModelAdmin, UserAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class CustomGroupAdmin(CustomModelAdmin, GroupAdmin):
    pass


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)


class AttachmentResource(resources.ModelResource):
    class Meta:
        model = Attachment


class AttachmentAdmin(CustomModelAdmin):
    resource_class = AttachmentResource
    search_fields = ['name', ' file', ]


admin.site.register(Attachment, AttachmentAdmin)


class OrgGroupResource(resources.ModelResource):
    class Meta:
        model = OrgGroup


class OrgGroupAdmin(CustomModelAdmin):
    resource_class = OrgGroupResource


admin.site.register(OrgGroup, OrgGroupAdmin)

