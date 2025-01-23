from api.serializers import ShaniModelSerializer
from .models import SiteSettings, DisplayItem, Page, Category, Catalog, Event


class DisplayItemSerializer(ShaniModelSerializer):
    class Meta:
        model = DisplayItem
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'link', 'image', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class EventSerializer(ShaniModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'time', 'link', 'image', 'org_group',
                  'created_at', 'updated_at', 'published', 'is_public', ]


class PageSerializer(ShaniModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'iframe_link',
                  'document_file', 'html_file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class CategorySerializer(ShaniModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'pages',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class CatalogSerializer(ShaniModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'sort_order', 'name', 'summary', 'description', 'image', 'display_items', 'categories',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class SiteSettingsSerializer(ShaniModelSerializer):
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
