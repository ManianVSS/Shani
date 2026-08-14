from django.urls import include, path
from rest_framework import routers

from .views import SiteSettingsViewSet, DisplayItemViewSet, get_all_site_details_api, SiteConfigPageViewSet, \
    get_default_site_details_api, SiteConfigCategoryViewSet, SiteConfigCatalogViewSet, EventViewSet

router = routers.DefaultRouter()

router.register(r'display_items', DisplayItemViewSet)
router.register(r'events', EventViewSet)
router.register(r'pages', SiteConfigPageViewSet)
router.register(r'categories', SiteConfigCategoryViewSet)
router.register(r'catalogs', SiteConfigCatalogViewSet)
router.register(r'site_settings', SiteSettingsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/site_details', get_all_site_details_api),
    path('api/default_site_details', get_default_site_details_api),
]
