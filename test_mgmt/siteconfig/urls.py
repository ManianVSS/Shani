from django.urls import include, path
from rest_framework import routers

from siteconfig.views import SiteSettingsViewSet, DisplayItemViewSet, get_site_details

router = routers.DefaultRouter()

router.register(r'display_items', DisplayItemViewSet)
router.register(r'site_settings', SiteSettingsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/site_details', get_site_details),
]
