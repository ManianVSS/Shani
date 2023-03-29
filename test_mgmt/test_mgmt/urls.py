from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from test_mgmt import settings

urlpatterns = [
                  path('admin/', include('massadmin.urls')),
                  path('admin/', admin.site.urls),
                  # For Advanced filters path('advanced_filters/', include('advanced_filters.urls')),
                  path('api/', include('api.urls')),
                  path('siteconfig/', include('siteconfig.urls')),
                  path('automation/', include('automation.urls')),
                  path('testdesign/', include('testdesign.urls')),
                  re_path('(^(?!(api|admin|data|automation|testdesign)).*$)',
                          TemplateView.as_view(template_name='index.html')),
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATICFILES_DIRS) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
