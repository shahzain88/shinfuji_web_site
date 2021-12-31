from django.urls import path
from . import views

app_name = "privacy"

urlpatterns = [
    path('', views.privacy_list, name="list"),
]
