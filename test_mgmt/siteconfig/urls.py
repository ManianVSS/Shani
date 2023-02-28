from django.urls import include, path
from rest_framework import routers

from siteconfig.views import SiteSettingsViewSet

router = routers.DefaultRouter()

router.register(r'site_settings', SiteSettingsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
