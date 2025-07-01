from django.urls import path
from .views import health_check, plate_logs

urlpatterns = [
    path('health/', health_check),
    path('plates/', plate_logs),
]
