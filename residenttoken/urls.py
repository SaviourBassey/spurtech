from django.urls import path
from .import views

app_name = "residenttoken"

urlpatterns = [
    path("generate-resident-token/", views.GenerateResidentToken.as_view(), name="generate_resident_token_view"),
    path("verify-resident-token/", views.VerifyResidentToken.as_view(), name="verify_resident_token_view"),
]
