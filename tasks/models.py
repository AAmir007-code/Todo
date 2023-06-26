from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    descript = models.TextField()
    task_image = models.ImageField(upload_to='images', null=True, blank=True)
    task_created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Bajariladigan_ish'
        verbose_name_plural = "Ishlar"


    def __str__(self):
        return self.title

    def get_time_diff(self):
        return self.deadline - self.task_created_date <= 0