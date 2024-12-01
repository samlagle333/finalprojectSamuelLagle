from django.db import models

class Threat(models.Model):
    threat_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    bookmarked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
