from django.db import models
from django.core import validators


class Feedback(models.Model):
    name = models.CharField(max_length=20, validators=[validators.MinLengthValidator(2)])
    surname = models.CharField(max_length=30)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
