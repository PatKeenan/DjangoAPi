from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    project_title = models.CharField(verbose_name="Project Title", max_length=100)
    project_description = models.TextField(verbose_name="Project Description", max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.project_title


    
class Task(models.Model):


    priority_level = [
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low'),
        ('4', 'Not Important'),
    ]

    status_choices = [
        ('Done', 'Done'),
        ('In Progress', 'In Progress'),
        ('Stuck', 'Stuck'),
        ('Next Up', 'Next Up'),
        ('Pending', 'Pending'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(verbose_name="Task Title", max_length=200)
    notes = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)
    scheduled_done = models.DateField(verbose_name="Scheduled to be done by:")
    status = models.CharField(max_length=20, choices=status_choices, default="Pending") 
    priority = models.CharField(
        max_length=1, choices=priority_level, default="4")

    class Meta:
        ordering = ['date_added']
    def __str__(self):
        return self.task
    


