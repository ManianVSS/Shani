from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from test_mgmt import settings

schema_view = get_schema_view(title='Test Management API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
                  path('admin/', include('massadmin.urls')),
                  path('admin/', admin.site.urls),
                  # For Advanced filters path('advanced_filters/', include('advanced_filters.urls')),
                  path('api/', include('api.urls')),
                  path('siteconfig/', include('siteconfig.urls')),
                  path('automation/', include('automation.urls')),
                  path('testdesign/', include('testdesign.urls')),
                  path('requirements/', include('requirements.urls')),
                  path('swagger/', schema_view, name='docs'),
                  re_path('(^(?!(api|admin|data|automation|requirements|testdesign|swagger)).*$)',
                          TemplateView.as_view(template_name='index.html')),
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATICFILES_DIRS) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
