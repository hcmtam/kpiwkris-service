from django.db import models
from django.db.models import JSONField
import uuid


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    userEmail = models.EmailField(unique=True)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    profilePic = models.URLField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userEmail


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sessionName = models.CharField(max_length=255)
    sessionId = models.CharField(max_length=255, unique=True)
    content = JSONField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sessionId
