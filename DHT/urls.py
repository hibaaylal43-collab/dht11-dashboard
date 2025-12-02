from django.urls import path
from . import views
from .api import Dlist, Dhtviews   # <-- cleaner imports

urlpatterns = [
    path("api/", Dlist, name='api_list'),
    path("api/post/", Dhtviews.as_view(), name='api_post'),

    path("", views.dashboard, name="dashboard"),
    path("latest/", views.latest_json, name="latest_json"),
    path('send-alert/', views.send_alert, name='send_alert'),
    path('graph_temp/', views.graph_temp, name='graph_temp'),
    path('graph_hum/', views.graph_hum, name='graph_hum'),
]



