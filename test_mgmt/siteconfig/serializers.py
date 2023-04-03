from rest_framework import serializers

from .models import SiteSettings, DisplayItem, Page, Category, Catalog


class DisplayItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayItem
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'link', 'image', 'org_group', 'published', ]


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'iframe_link',
                  'org_group', 'published', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'pages',
                  'org_group', 'published', ]


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'categories',
                  'org_group', 'published', ]


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'email', 'logo', 'image', 'catalogs',
                  'org_group', 'published', ]
