from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path('', views.contact_create_list, name="create_list"),
    # path('thank-you/', views.contact_thank_you, name="thank_you"),
    path('view_list', views.contact_view_list, name="view_list"),
    path('<slug:slug>/', views.contact_view_detail, name="view_detail"),
]
