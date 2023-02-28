import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from revproxy.views import ProxyView

from test_mgmt import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('api.urls')),
                  # re_path(r'(mapi.*)', ProxyView.as_view(upstream='http://localhost:27010/')), # Reverse proxy use
                  re_path('(^(?!(api|admin|data)).*$)', TemplateView.as_view(template_name='index.html')),
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATICFILES_DIRS) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if DEBUG else settings.STATIC_ROOT
