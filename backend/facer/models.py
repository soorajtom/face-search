from email.policy import default
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Search(models.Model):
    uuid = models.TextField(max_length=64, null=True, blank=True)
    search_img = models.ImageField(upload_to='search/')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    results = models.JSONField(default=list)