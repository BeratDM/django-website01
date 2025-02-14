from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
from . import views

app_name = "accounts"
urlpatterns = [
    # Django Auth
    path(
        "login",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=CustomLoginForm,
        ),
        name="login",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("profile", views.ProfileView.as_view(), name="profile"),
]
