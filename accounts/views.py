from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from residenttoken.models import ResidentToken


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/register.html")
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        estate_name = request.POST.get("estate_name")
        state = request.POST.get("state")
        if User.objects.filter(email=email).exists():
            message = "The email is already registered"
            return redirect("accounts:register_view")
        else:
            new_user = User.objects.create_user(username=email, email=email, password=password)
            new_user.save()
            return redirect("accounts:login_view")
        

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/login.html")
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email).exists():
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages = f"Welcome back {email}"
                return redirect("accounts:resident_dashboard_view")
            else:
                print("not finally")
                message = "Incorrect credentials "
                return redirect("accounts:login_view")
        else:
            message = "No account with that credentials"
            return redirect("accounts:login_view")


class AdminLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/admin-login.html")
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                messages = f"Welcome back {username}"
                return redirect("accounts:admin_dashboard_view")
            else:
                print("not finally")
                message = "Incorrect credentials "
                return redirect("accounts:admin_login_view")
        else:
            message = "No account with that credentials"
            return redirect("accounts:admin_login_view")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        message = "You've logged out"
        return redirect("home:home_view")


class ResidentDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            token = ResidentToken.objects.filter(user=request.user).order_by("-timestamp").first()
        except:
            token = None
        context = {
            "token":token
        }
        return render(request, "accounts/resident-dashboard.html", context)
    

class AdminDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/admin-dashboard.html")