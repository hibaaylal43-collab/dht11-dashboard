from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('latest/', views.latest_json, name='latest'),
    path('graph_temp/', views.graph_temp, name='graph_temp'),  # ADD THIS
    path('graph_hum/', views.graph_hum, name='graph_hum'),      # ADD THIS
    path('api/', views.api_data, name='api_data'),              # ADD THIS
    path('send-alert/', views.send_alert, name='send_alert'),
]
