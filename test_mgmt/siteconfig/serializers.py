from rest_framework import serializers

from .models import SiteSettings, DisplayItem, Page


class DisplayItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayItem
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'link', 'image', ]


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', ]


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'email', 'logo', 'image', 'display_items',
                  'pages', ]
