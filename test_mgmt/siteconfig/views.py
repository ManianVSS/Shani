from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups
from siteconfig.models import SiteSettings, DisplayItem
from siteconfig.serializers import SiteSettingsSerializer, DisplayItemSerializer


class DisplayItemViewSet(viewsets.ModelViewSet):
    queryset = DisplayItem.objects.all()
    serializer_class = DisplayItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'sort_order', 'name', 'summary', ]
    ordering = ['id', 'sort_order', 'name']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'sort_order': compare_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }


class SiteSettingsViewSet(viewsets.ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'email', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'email': string_fields_filter_lookups,
    }


@api_view(['GET'])
def get_site_details(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    site_settings_id = 1
    if 'site_settings' in request.GET:
        site_settings_id = int(request.query_params.get('site_settings'))

    try:
        site_settings = SiteSettings.objects.get(pk=site_settings_id)
    except SiteSettings.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='Could not find site_settings passed')

    display_items = []
    for display_item_info in site_settings.display_items.all().order_by('sort_order'):
        display_items.append({
            "id": display_item_info.id,
            "sort_order": display_item_info.sort_order,
            "name": display_item_info.name,
            "summary": display_item_info.summary,
            "description": display_item_info.description,
            "link": display_item_info.link,
            'image': DisplayItemSerializer(site_settings).data['image'],
        })

    site_details = {
        "id": site_settings.id,
        'name': site_settings.name,
        'summary': site_settings.summary,
        'description': site_settings.description,
        'email': site_settings.email,
        'logo': SiteSettingsSerializer(site_settings).data['logo'],
        'display_items': display_items,
    }

    return Response(site_details)
