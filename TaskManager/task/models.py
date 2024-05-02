from django.db import models

# Create your models here.
class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Personal', 'Personal'),
        ('Trabajo', 'Trabajo'),
        ('Estudio', 'Estudio'),
        ('Otros', 'Otros'),
    ]

    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False, max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False)
    deadline = models.DateTimeField(blank=False, null=False)
    completed = models.BooleanField(default=False, blank=False)
    