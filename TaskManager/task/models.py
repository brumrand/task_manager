from django.db import models

# Create your models here.
class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Personal', 'Personal'),
        ('Trabajo', 'Trabajo'),
        ('Estudio', 'Estudio'),
        ('Otros', 'Otros'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)