from django.urls import path
from . import views

urlpatterns = [
    #path("password_reset_form/", signup, name="signup"),
    path("signup/", views.signup, name="signup"),
    path("employee_list/", views.employee_list, name="employee_list"),
    path('employee_detail/<int:pk>/', views.employee_detail, name='employee_detail'),
]