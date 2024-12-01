from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    result = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.query}"
