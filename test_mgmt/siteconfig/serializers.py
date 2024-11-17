from rest_framework import serializers

from .models import SiteSettings, DisplayItem, Page, Category, Catalog, Event


class DisplayItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayItem
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'link', 'image', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'time', 'link', 'image', 'org_group',
                  'created_at', 'updated_at', 'published', 'is_public', ]


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'iframe_link',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'pages',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'categories',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'email', 'logo', 'image', 'catalogs',
                  'org_group', 'published', ]


serializer_map = {
    DisplayItem: DisplayItemSerializer,
    Event: EventSerializer,
    Page: PageSerializer,
    Category: CategorySerializer,
    Catalog: CatalogSerializer,
    SiteSettings: SiteSettingsSerializer,
}
