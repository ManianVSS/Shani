from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
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
                return not hasattr(obj, 'can_read') or obj.can_read(request.user)
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
                return not hasattr(obj, 'can_modify') or obj.can_modify(request.user)
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
                return not hasattr(obj, 'can_delete') or obj.can_delete(request.user)
            except FieldDoesNotExist:
                return True
        else:
            return False

    # Allow only listing of entities that can be viewed by the user
    def get_queryset(self, request):
        if request.user is None:
            return self.model.objects.none()
        else:
            return self.model.objects.all()

        # if request.user.is_superuser or not hasattr(self.model, 'can_read'):
        #     return self.model.objects.all()

        # try:
        #     can_view_filter = [obj.id for obj in self.model.objects.all() if obj.can_read(request.user)]
        #     return self.model.objects.filter(id__in=can_view_filter)
        # except FieldDoesNotExist:
        #     return self.model.objects.all()
        # except Exception as e:
        #     print(str(e))
        #     return self.model.objects.none()


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

    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
    )


admin.site.register(Attachment, AttachmentAdmin)


class OrgGroupResource(resources.ModelResource):
    class Meta:
        model = OrgGroup


class OrgGroupAdmin(CustomModelAdmin):
    resource_class = OrgGroupResource
    list_filter = (
        'published',
        ('org_group', RelatedOnlyFieldListFilter),
        ('leaders', RelatedOnlyFieldListFilter),
        ('members', RelatedOnlyFieldListFilter),
        ('guests', RelatedOnlyFieldListFilter),
    )

    search_fields = ['name', 'summary', 'description', ]


admin.site.register(OrgGroup, OrgGroupAdmin)
