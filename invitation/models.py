from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    qr_code = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.name} {self.email}"

    class Meta: 
        ordering = ['name', 'email']
    
