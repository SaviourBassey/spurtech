from django.urls import path
from .import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register_view"),
    path("login/", views.LoginView.as_view(), name="login_view"),
    path("admin-login/", views.AdminLoginView.as_view(), name="admin_login_view"),
    path("logout/", views.LogoutView.as_view(), name="logout_view"),
    path("resident-dashboard/", views.ResidentDashboardView.as_view(), name="resident_dashboard_view"),
    path("admin-dashboard/", views.AdminDashboardView.as_view(), name="admin_dashboard_view"),
]
