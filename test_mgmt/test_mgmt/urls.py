from django.conf.urls.static import static
from django.urls import include, path
from django.urls import re_path
from django.views.generic import TemplateView
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from api import admin
from . import settings

# schema_view = get_schema_view(title='Test Management API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

schema_view = get_schema_view(
    openapi.Info(
        title="Test Management API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://github.com/manianvss/shani?tab=BSD-3-Clause-1-ov-file#readme",
        contact=openapi.Contact(email="manianvss@hotmail.com"),
        license=openapi.License(name="BSD-3-Clause license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

# noinspection PyUnresolvedReferences
urlpatterns = [
    # Admin plugins and other libraries
    path('admin/', include('massadmin.urls')),
    path('admin/', admin.site.urls),
    # For Advanced filters path('advanced_filters/', include('advanced_filters.urls')),

    # Modules
    path('api/', include('api.urls')),
    path('siteconfig/', include('siteconfig.urls')),
    path('requirements/', include('requirements.urls')),
    path('workitems/', include('workitems.urls')),
    path('scheduler/', include('scheduler.urls')),
    path('testdesign/', include('testdesign.urls')),
    path('automation/', include('automation.urls')),
    path('execution/', include('execution.urls')),
    path('people/', include('people.urls')),
    path('program/', include('program.urls')),

    # Swagger
    # path('swagger/', schema_view, name='docs'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Trap code access (?(py|sh|bat|htaccess))
    re_path('(^.*[.](py|sh|bat|htaccess)$)',
            TemplateView.as_view(template_name='errors/forbidden.html')),

    re_path(
        '(^(?!(data|admin|swagger|api|siteconfig|requirements|workitems|scheduler|testdesign|automation|execution|people|program)).*$)',
        TemplateView.as_view(template_name='index.html')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for STATIC_URL in settings.STATIC_URLS:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
