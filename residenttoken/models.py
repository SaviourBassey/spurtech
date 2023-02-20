from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ResidentToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    expired = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)