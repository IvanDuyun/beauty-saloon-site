from django.urls import path
from .views import signup

urlpatterns = [
    path("password_reset_form/", signup, name="signup"),
    path("signup/", signup, name="signup"),
]