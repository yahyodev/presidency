from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class LevelChoices(models.TextChoices):
    beginner = 'Beginner', 'Beginner'
    elementary = 'Elementary', 'Elementary'
    pre_intermediate = 'Pre-Intermediate', 'Pre-Intermediate'
    intermediate = 'Intermediate', 'Intermediate'
    upper_intermediate = 'Upper-Intermediate', 'Upper-Intermediate'
    advanced = 'Advanced', 'Advanced'