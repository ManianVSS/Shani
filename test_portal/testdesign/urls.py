from django.urls import include, path
from rest_framework import routers

from .views import TestDesignAttachmentViewSet, TestDesignTagViewSet, TestDesignTestCaseCategoryViewSet, TestDesignTestCaseViewSet

router = routers.DefaultRouter()

router.register(r'attachments', TestDesignAttachmentViewSet)
router.register(r'tags', TestDesignTagViewSet)
router.register(r'testcasecategories', TestDesignTestCaseCategoryViewSet)
router.register(r'testcases', TestDesignTestCaseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
