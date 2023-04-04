from django.urls import include, path
from rest_framework import routers

from .views import AttachmentViewSet, TagViewSet, ReleaseViewSet, DefectViewSet, RunViewSet, ExecutionRecordViewSet, \
    ReliabilityRunViewSet, EnvironmentViewSet, get_ipte_for_iterations, get_iterations_for_ipte

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)

router.register(r'releases', ReleaseViewSet)
router.register(r'defects', DefectViewSet)
router.register(r'runs', RunViewSet)
router.register(r'execution_records', ExecutionRecordViewSet)
router.register(r'reliability_runs', ReliabilityRunViewSet)
router.register(r'environments', EnvironmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/ipte/ipte_for_iterations', get_ipte_for_iterations),
    path('api/ipte/iterations_for_ipte', get_iterations_for_ipte),
]
