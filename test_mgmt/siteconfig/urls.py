from django.urls import include, path
from rest_framework import routers

from .views import SiteSettingsViewSet, DisplayItemViewSet, get_all_site_details_api, PageViewSet, \
    get_default_site_details_api, CategoryViewSet, CatalogViewSet, EventViewSet

router = routers.DefaultRouter()

router.register(r'display_items', DisplayItemViewSet)
router.register(r'events', EventViewSet)
router.register(r'pages', PageViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'catalogs', CatalogViewSet)
router.register(r'site_settings', SiteSettingsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/site_details', get_all_site_details_api),
    path('api/default_site_details', get_default_site_details_api),
]
