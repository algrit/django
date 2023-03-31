from django.db import models
from django.core import validators


class Feedback(models.Model):
    name = models.CharField(max_length=20, validators=[validators.MinLengthValidator(2)])
    rating = models.PositiveIntegerField(validators=[validators.MaxValueValidator(10)])
    comment = models.TextField(validators=[validators.MinLengthValidator(1)])
