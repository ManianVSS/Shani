from django.urls import include, path
from rest_framework import routers

from .apiviews import generate_otp
from .views import AttachmentViewSet, TagViewSet, StepViewSet, PropertiesViewSet, MockAPIViewSet, \
    MockAPIRoutingViewSet, AuthenticatorSecretViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'steps', StepViewSet)
router.register(r'properties', PropertiesViewSet)

router.register(r'mockapi', MockAPIViewSet)
router.register(r'mockapi_call', MockAPIRoutingViewSet, basename='mock api call', )

router.register(r'authenticator_secrets', AuthenticatorSecretViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/authenticator', generate_otp),
]
