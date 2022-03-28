from django.db import models
from django.contrib.auth import get_user_model

TASK_STATUS = (
    ("Pending", "Pending"),
    ("Completed", "Completed"),
    ("Cancelled", "Cancelled"),
)

class Garden_Tasks(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices = TASK_STATUS,
    default = "Pending")
    gardener = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, related_name="Garden_Tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




