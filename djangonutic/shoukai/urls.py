from django.urls import path
from . import views

app_name = "shoukai"

urlpatterns = [
    path('', views.shoukai_list, name="list"),
]
