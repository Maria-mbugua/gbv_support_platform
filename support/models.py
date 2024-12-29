from django.db import models
from django.contrib.auth.models import User

class GBVCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    anonymous = models.BooleanField(default=False)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

class IncidentReport(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Closed', 'Closed'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    recommendation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description[:50]


