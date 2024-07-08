from django.forms import ModelForm
from .models import Food, Goals, Exercise, Weight


class CreateFoodItem(ModelForm):
    class Meta:
        model = Food
        fields = ('item_name', 'calories_amount', 'date')

class CreateExercise(ModelForm):
    class Meta:
        model = Exercise
        fields = ('exercise_name', 'calories_burned', 'date')

class CreateWeight(ModelForm):
    class Meta:
        model = Weight
        fields = ('weight', 'date')


class UpdateGoal(ModelForm):
    class Meta:
        model = Goals
        fields = ('goal_calories_eaten_per_day', 'goal_calories_burned_per_day', 'goal_weight')
