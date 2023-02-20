from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ResidentToken
from .generate_token import gen_token
from django.http import JsonResponse

# Create your views here.

class GenerateResidentToken(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        token = None
        if ResidentToken.objects.filter(user=request.user).exists():
            ResidentToken.objects.filter(user=request.user).delete()
            token = ResidentToken.objects.create(user=request.user, token=gen_token())
        else:
            token = ResidentToken.objects.create(user=request.user, token=gen_token())
        data = {
            "token":token.token,
        }
        return JsonResponse(data)