from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


STATUS_CHOICES = (
    ('watching', 'WATCHING'),
    ('plan_to_watch', 'PLAN TO WATCH'),
    ('completed', 'COMPLETED'),
)


class Anime(models.Model):

    name = models.CharField(max_length=250)
    japanese_name = models.CharField(max_length=250)
    description = models.TextField()
    score = models.IntegerField(default=10, validators=[
                                MinValueValidator(1), MaxValueValidator(10)])
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    episodes = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='plan_to_watch')

    def __str__(self):
        return self.name
