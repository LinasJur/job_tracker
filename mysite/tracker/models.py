from django.contrib.auth.models import User
from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("saved", "Išsaugotas"),
        ("applied", "Kandidatuota"),
        ("interview", "Interviu"),
        ("rejected", "Atmesta"),
        ("accepted", "Priimta"),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    job_link = models.URLField(blank=True)
    salary = models.CharField(max_length=50, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="saved"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class Note(models.Model):
    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.content