from django.urls import path
from . import views

app_name = "recruitment"

urlpatterns = [
    path('', views.recruitment_list, name="list"),
]
