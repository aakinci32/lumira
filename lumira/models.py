from django.db import models
from django.contrib.auth.models import User

class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availability')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.date} ({self.start_time} - {self.end_time})"
