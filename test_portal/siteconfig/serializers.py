from api.models import org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import SiteSettings, DisplayItem, Page, Category, Catalog, Event


class DisplayItemSerializer(ShaniModelSerializer):
    class Meta:
        model = DisplayItem
        fields = org_model_base_fields + ['sort_order', 'name', 'summary', 'description', 'link', 'image', ]


class EventSerializer(ShaniModelSerializer):
    class Meta:
        model = Event
        fields = org_model_base_fields + ['sort_order', 'name', 'summary', 'description', 'time', 'link', 'image', ]


class PageSerializer(ShaniModelSerializer):
    class Meta:
        model = Page
        fields = org_model_base_fields + ['sort_order', 'name', 'summary', 'description', 'image', 'display_items',
                                          'iframe_link', 'document_file', 'html_file', ]


class CategorySerializer(ShaniModelSerializer):
    class Meta:
        model = Category
        fields = org_model_base_fields + ['sort_order', 'name', 'summary', 'description', 'image', 'display_items',
                                          'pages', ]


class CatalogSerializer(ShaniModelSerializer):
    class Meta:
        model = Catalog
        fields = org_model_base_fields + ['sort_order', 'name', 'summary', 'description', 'image', 'display_items',
                                          'categories', ]


class SiteSettingsSerializer(ShaniModelSerializer):
    class Meta:
        model = SiteSettings
        fields = org_model_base_fields + ['sort_order', 'name', 'summary', 'description', 'email', 'logo', 'image',
                                          'catalogs',
                                          ]


serializer_map = {
    DisplayItem: DisplayItemSerializer,
    Event: EventSerializer,
    Page: PageSerializer,
    Category: CategorySerializer,
    Catalog: CatalogSerializer,
    SiteSettings: SiteSettingsSerializer,
}
