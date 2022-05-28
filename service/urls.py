from django.urls import path
from . import views

urlpatterns = [
    path("", views.service_list, name="service_list"),
    path("service/<int:pk>/edit/", views.service_edit, name="service_edit"),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('service/new/', views.service_new, name='service_new'),
]