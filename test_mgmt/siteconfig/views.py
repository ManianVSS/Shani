from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import OrgGroupSerializer
from api.views import default_search_fields, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups
from siteconfig.models import SiteSettings, DisplayItem, Page
from siteconfig.serializers import SiteSettingsSerializer, DisplayItemSerializer, PagesSerializer


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


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'sort_order', 'name', 'summary', ]
    ordering = ['sort_order', 'id', 'name']
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
    ordering_fields = ['id', 'sort_order', 'name', 'summary', 'email', ]
    ordering = ['sort_order', 'id', 'name']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'sort_order': compare_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'email': string_fields_filter_lookups,
    }


@api_view(['GET'])
def get_site_details(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    all_sites_details = []
    for site_settings in SiteSettings.objects.all().order_by('sort_order'):
        all_pages = []
        for page in site_settings.pages.all().order_by('sort_order'):
            display_items = []
            for display_item_info in page.display_items.all().order_by('sort_order'):
                display_items.append({
                    "id": display_item_info.id,
                    "sort_order": display_item_info.sort_order,
                    "name": display_item_info.name,
                    "summary": display_item_info.summary,
                    "description": display_item_info.description,
                    "link": display_item_info.link,
                    'image': DisplayItemSerializer(display_item_info).data['image'],
                    "org_group": OrgGroupSerializer(display_item_info.org_group).data[
                        'id'] if display_item_info.org_group else None,
                })
            page_details = {
                "id": page.id,
                'sort_order': page.sort_order,
                'name': page.name,
                'summary': page.summary,
                'description': page.description,
                'image': PagesSerializer(page).data['image'],
                'display_items': display_items,
                "org_group": OrgGroupSerializer(page.org_group).data['id'] if page.org_group else None,
            }
            all_pages.append(page_details)

        site_details = {
            "id": site_settings.id,
            'sort_order': site_settings.sort_order,
            'name': site_settings.name,
            'summary': site_settings.summary,
            'description': site_settings.description,
            'email': site_settings.email,
            'logo': SiteSettingsSerializer(site_settings).data['logo'],
            'pages': all_pages,
            "org_group": OrgGroupSerializer(site_settings.org_group).data['id'] if site_settings.org_group else None,
        }
        all_sites_details.append(site_details)

    return Response(all_sites_details)
