from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(max_length=500, blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)