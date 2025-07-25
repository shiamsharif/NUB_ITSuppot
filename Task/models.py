# tasks/models.py
from django.db import models
from Account.models import CustomUser  

class Task(models.Model):
    ISSUE_CHOICES = [
        ('software', 'Software Issues'),
        ('hardware', 'Hardware Issues'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    
    room_number = models.CharField(max_length=20)
    computer_id = models.CharField(max_length=100, blank=True, null=True)
    monitor_id = models.CharField(max_length=100, blank=True, null=True)
    ups_id = models.CharField(max_length=100, blank=True, null=True)

    issues = models.CharField(max_length=100, blank=True, null=True)
    issues_type = models.CharField(max_length=10, choices=ISSUE_CHOICES, default='None')
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.issues_type}"