from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, ManyRelatedField

from .models import Attachment, OrgGroup, Configuration, Site


class ShaniModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        self.expand_relation_as_object = kwargs.pop('expand_relation_as_object', True)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        super_representation = super().to_representation(instance)

        if self.expand_relation_as_object:
            fields = self._readable_fields

            for field in fields:
                attribute = field.get_attribute(instance)
                instance_field = getattr(instance, field.field_name)
                if instance_field:
                    if isinstance(field, PrimaryKeyRelatedField):
                        if hasattr(instance_field, 'to_relation_representation'):
                            super_representation[field.field_name] = instance_field.to_relation_representation()
                        else:
                            super_representation[field.field_name] = {'id': instance_field.id, }
                    elif isinstance(field, ManyRelatedField):
                        super_representation[field.field_name] = []
                        for related_item in instance_field.all():
                            if hasattr(related_item, 'to_relation_representation'):
                                repr_item_to_add = related_item.to_relation_representation()
                            else:
                                repr_item_to_add = {'id': related_item.id, }
                            super_representation[field.field_name].append(repr_item_to_add)

        return super_representation


class UserSerializer(ShaniModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined',
                  'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', ]


class GroupSerializer(ShaniModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


class ConfigurationSerializer(ShaniModelSerializer):
    class Meta:
        model = Configuration
        fields = ['id', 'name', 'value', 'description', 'created_at', 'updated_at', 'published', 'is_public', ]


class OrgGroupSerializer(ShaniModelSerializer):
    class Meta:
        model = OrgGroup
        fields = ['id', 'name', 'summary', 'auth_group', 'description', 'org_group', 'leaders', 'members', 'guests',
                  'consumers', 'created_at', 'updated_at', 'published', 'is_public', ]


class AttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class SiteSerializer(ShaniModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public',
                  'attachments', ]


serializer_map = {
    User: UserSerializer,
    Group: GroupSerializer,
    Configuration: ConfigurationSerializer,
    OrgGroup: OrgGroupSerializer,
    Attachment: AttachmentSerializer,
    Site: SiteSerializer,
}
