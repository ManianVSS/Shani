from rest_framework import serializers

from .models import SiteSettings, DisplayItem


class DisplayItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayItem
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'link', 'image', ]


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['id', 'name', 'summary', 'description', 'email', 'logo', 'display_items', ]
