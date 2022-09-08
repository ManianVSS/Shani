from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from test_mgmt import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('api.urls')),

                  re_path('(^(?!(api|admin|media)).*$)', TemplateView.as_view(template_name='index.html')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
