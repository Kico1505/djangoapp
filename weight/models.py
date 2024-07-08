import datetime
from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    item_name = models.CharField(max_length=100, null=True)
    calories_amount = models.IntegerField(default=0, null=True)
    date = models.DateField(default=datetime.date.today, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item_name


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100, null=True)
    calories_burned = models.IntegerField(default=0, null=True)
    date = models.DateField(default=datetime.date.today, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.exercise_name


class Weight(models.Model):
    weight = models.IntegerField(default=250, null=True)
    date = models.DateField(default=datetime.date.today, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Goals(models.Model):
    goal_calories_eaten_per_day = models.IntegerField(default=2000)
    goal_calories_burned_per_day = models.IntegerField(default=200)
    goal_weight = models.IntegerField(default=180)
    date = models.DateField(default=datetime.date.today, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

