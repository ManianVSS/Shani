from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import OrgGroupSerializer
from api.views import default_search_fields, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups, exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet
from .models import SiteSettings, DisplayItem, Page, Category, Catalog, get_default_settings
from .serializers import SiteSettingsSerializer, DisplayItemSerializer, PageSerializer, CatalogSerializer, \
    CategorySerializer


class DisplayItemViewSet(ShaniOrgGroupViewSet):
    queryset = DisplayItem.objects.all()
    serializer_class = DisplayItemSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'sort_order', 'name', 'summary', 'org_group', 'published', ]
    ordering = ['id', 'sort_order', 'name']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'sort_order': compare_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


class PageViewSet(ShaniOrgGroupViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'sort_order', 'name', 'summary', 'org_group', 'published', ]
    ordering = ['sort_order', 'id', 'name']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'sort_order': compare_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


class CategoryViewSet(ShaniOrgGroupViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'sort_order', 'name', 'summary', 'org_group', 'published', ]
    ordering = ['sort_order', 'id', 'name']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'sort_order': compare_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


class CatalogViewSet(ShaniOrgGroupViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'sort_order', 'name', 'summary', 'org_group', 'published', ]
    ordering = ['sort_order', 'id', 'name']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'sort_order': compare_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


class SiteSettingsViewSet(ShaniOrgGroupViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'sort_order', 'name', 'summary', 'email', 'org_group', 'published', ]
    ordering = ['sort_order', 'id', 'name']
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'sort_order': compare_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'email': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


@api_view(['GET'])
def get_all_site_details_api(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    all_sites_details = get_all_site_settings()
    return Response(all_sites_details)


@api_view(['GET'])
def get_default_site_details_api(request):
    if not request.method == 'GET':
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    default_site_settings = get_default_settings()
    all_sites_details = get_site_settings_as_dict(default_site_settings)
    return Response(all_sites_details)


def get_all_site_settings():
    all_site_settings = []
    for site_settings in SiteSettings.objects.filter(published=True).order_by('sort_order'):
        site_details = get_site_settings_as_dict(site_settings)
        all_site_settings.append(site_details)
    return all_site_settings


def get_site_settings_as_dict(site_settings):
    site_details = {
        "id": site_settings.id,
        'sort_order': site_settings.sort_order,
        'name': site_settings.name,
        'summary': site_settings.summary,
        'description': site_settings.description,
        'email': site_settings.email,
        'logo': SiteSettingsSerializer(site_settings).data['logo'],
        'image': SiteSettingsSerializer(site_settings).data['image'],
        'catalogs': get_catalog_details_for_site_settings(site_settings),
        "org_group": OrgGroupSerializer(site_settings.org_group).data['id'] if site_settings.org_group else None,
        "published": site_settings.published,
    }
    return site_details


def get_catalog_details_for_site_settings(site_settings):
    all_catalogs_detail = []
    if site_settings.catalogs is not None:
        for catalog in site_settings.catalogs.filter(published=True).order_by('sort_order'):
            category_detail = get_catalog_as_dict(catalog)
            all_catalogs_detail.append(category_detail)

    return all_catalogs_detail


def get_catalog_as_dict(catalog):
    return {
        "id": catalog.id,
        'sort_order': catalog.sort_order,
        'name': catalog.name,
        'summary': catalog.summary,
        'description': catalog.description,
        'image': CatalogSerializer(catalog).data['image'],
        'display_items': get_entity_display_items(catalog),
        'categories': get_category_details_for_catalog(catalog),
        "org_group": OrgGroupSerializer(catalog.org_group).data['id'] if catalog.org_group else None,
        "published": catalog.published,
    }


def get_category_details_for_catalog(catalog):
    all_categories_detail = []
    if catalog.categories is not None:
        for category in catalog.categories.filter(published=True).order_by('sort_order'):
            category_detail = get_category_as_dict(category)
            all_categories_detail.append(category_detail)

    return all_categories_detail


def get_category_as_dict(category):
    return {
        "id": category.id,
        'sort_order': category.sort_order,
        'name': category.name,
        'summary': category.summary,
        'description': category.description,
        'image': CategorySerializer(category).data['image'],
        'display_items': get_entity_display_items(category),
        'pages': get_page_details_for_category(category),
        "org_group": OrgGroupSerializer(category.org_group).data['id'] if category.org_group else None,
        "published": category.published,
    }


def get_page_details_for_category(category):
    all_pages = []
    if category.pages is not None:
        for page in category.pages.filter(published=True).order_by('sort_order'):
            page_details = get_page_as_dict(page)
            all_pages.append(page_details)
    return all_pages


def get_page_as_dict(page):
    return {
        "id": page.id,
        'sort_order': page.sort_order,
        'name': page.name,
        'summary': page.summary,
        'description': page.description,
        'image': PageSerializer(page).data['image'],
        'display_items': get_entity_display_items(page),
        'iframe_link': page.iframe_link,
        "org_group": OrgGroupSerializer(page.org_group).data['id'] if page.org_group else None,
        "published": page.published,
    }


def get_entity_display_items(entity):
    display_items = []
    if entity.display_items is not None:
        for display_item_info in entity.display_items.filter(published=True).order_by('sort_order'):
            display_items.append(get_display_item_as_dict(display_item_info))
    return display_items


def get_display_item_as_dict(display_item_info):
    return {
        "id": display_item_info.id,
        "sort_order": display_item_info.sort_order,
        "name": display_item_info.name,
        "summary": display_item_info.summary,
        "description": display_item_info.description,
        "link": display_item_info.link,
        'image': DisplayItemSerializer(display_item_info).data['image'],
        "org_group": OrgGroupSerializer(display_item_info.org_group).data[
            'id'] if display_item_info.org_group else None,
        "published": display_item_info.published,
    }
