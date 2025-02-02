from django.urls import include, path
from rest_framework import routers

from .apiviews import start_run, stop_run, start_reliability_run, stop_reliability_run
from .views import AttachmentViewSet, TagViewSet, ReleaseViewSet, DefectViewSet, RunViewSet, ExecutionRecordViewSet, \
    ReliabilityRunViewSet, EnvironmentViewSet, get_ipte_for_iterations, get_iterations_for_ipte, BuildViewSet, \
    ReliabilityIterationViewSet, ReliabilityIncidentViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)

router.register(r'releases', ReleaseViewSet)
router.register(r'builds', BuildViewSet)
router.register(r'defects', DefectViewSet)
router.register(r'runs', RunViewSet)
router.register(r'execution_records', ExecutionRecordViewSet)
router.register(r'reliability_incidents', ReliabilityIncidentViewSet)
router.register(r'reliability_runs', ReliabilityRunViewSet)
router.register(r'reliability_iterations', ReliabilityIterationViewSet)
router.register(r'environments', EnvironmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/ipte/ipte_for_iterations', get_ipte_for_iterations),
    path('api/ipte/iterations_for_ipte', get_iterations_for_ipte),

    path('api/start_run', start_run),
    path('api/stop_run', stop_run),

    path('api/start_reliability_run', start_reliability_run),
    path('api/stop_reliability_run', stop_reliability_run),
]
