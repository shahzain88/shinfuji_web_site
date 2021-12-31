from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("signup/", views.account_signup, name="signup"),
    path("login/", views.account_login, name="login"),
    path("logout/", views.account_logout, name="logout"),
]
