from rest_framework import serializers

from siteconfig.models import SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['id', 'name', 'summary', 'description', 'email', ]
