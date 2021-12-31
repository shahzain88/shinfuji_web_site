from django.urls import path
from . import views

app_name = "QandA"

urlpatterns = [
    path('', views.QandA_list, name="list"),
]
