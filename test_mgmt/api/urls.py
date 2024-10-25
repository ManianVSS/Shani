from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import UserViewSet, GroupViewSet, AttachmentViewSet, OrgGroupViewSet, PropertiesViewSet, \
    ConfigurationViewSet, SiteViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

router.register(r'configuration', ConfigurationViewSet)
router.register(r'org_groups', OrgGroupViewSet)

router.register(r'attachments', AttachmentViewSet)
router.register(r'properties', PropertiesViewSet)
router.register(r'sites', SiteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('usecases_count', use_case_count),
    # path('requirement_count', requirement_count),
    # path('testcases_count', test_case_count),

    path('auth/restframework', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/jwt/login', jwt_views.TokenObtainPairView.as_view()),
    path('auth/jwt/refresh', jwt_views.TokenRefreshView.as_view()),

    # path('score/', get_score),
    # path('use_case_category_score/<int:pk>', get_use_case_category_score),
    # path('use_case_score/<int:pk>', get_use_case_score),
    # path('use_case_completion/<int:pk>', get_use_case_completion),
    # path('use_case_category_completion/<int:pk>', get_use_case_category_completion),
    # path('completion', get_overall_completion),
]
