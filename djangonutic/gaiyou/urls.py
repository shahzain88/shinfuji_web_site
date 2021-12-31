from django.urls import path
from . import views

app_name = "gaiyou"

urlpatterns = [
    path('', views.gaiyou_list, name="list"),
    path('map/', views.gaiyou_map, name="map")
]
