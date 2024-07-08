import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateFoodItem, UpdateGoal, CreateExercise, CreateWeight
from .models import Food, Goals, Exercise, Weight


# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    total_calories = 0
    dayone = datetime.date.today()
    daytwo = datetime.date.today() - datetime.timedelta(days=1)
    daythree = datetime.date.today() - datetime.timedelta(days=2)
    dayfour = datetime.date.today() - datetime.timedelta(days=3)
    dayfive = datetime.date.today() - datetime.timedelta(days=4)
    daysix = datetime.date.today() - datetime.timedelta(days=5)
    dayseven = datetime.date.today() - datetime.timedelta(days=6)
    one = Food.objects.filter(date__year=dayone.year, date__month=dayone.month, date__day=dayone.day, user=request.user)
    two = Food.objects.filter(date__year=daytwo.year, date__month=daytwo.month, date__day=daytwo.day, user=request.user)
    three = Food.objects.filter(date__year=daythree.year, date__month=daythree.month, date__day=daythree.day, user=request.user)
    four = Food.objects.filter(date__year=dayfour.year, date__month=dayfour.month, date__day=dayfour.day, user=request.user)
    five = Food.objects.filter(date__year=dayfive.year, date__month=dayfive.month, date__day=dayfive.day, user=request.user)
    six = Food.objects.filter(date__year=daysix.year, date__month=daysix.month, date__day=daysix.day, user=request.user)
    seven = Food.objects.filter(date__year=dayseven.year, date__month=dayseven.month, date__day=dayseven.day, user=request.user)

    caloriesone = 0
    caloriestwo = 0
    caloriesthree = 0
    caloriesfour = 0
    caloriesfive = 0
    caloriessix = 0
    calorieseven = 0

    for food in one:
        caloriesone += food.calories_amount

    for food in two:
        caloriestwo += food.calories_amount

    for food in three:
        caloriesthree += food.calories_amount

    for food in four:
        caloriesfour += food.calories_amount

    for food in five:
        caloriesfive += food.calories_amount

    for food in six:
        caloriessix += food.calories_amount

    for food in seven:
        calorieseven += food.calories_amount

    total_weekly_calories = caloriesone + caloriestwo + caloriesthree + caloriesfour + caloriesfive + caloriessix + calorieseven

    total = Food.objects.filter(user=request.user)

    for food in total:
            total_calories += food.calories_amount

    caloriegoal = Goals.objects.get(pk=request.user.id).goal_calories_eaten_per_day

    total_caloriese = 0

    onee = Exercise.objects.filter(date__year=dayone.year, date__month=dayone.month, date__day=dayone.day,
                                  user=request.user)
    twoe = Exercise.objects.filter(date__year=daytwo.year, date__month=daytwo.month, date__day=daytwo.day,
                                  user=request.user)
    threee = Exercise.objects.filter(date__year=daythree.year, date__month=daythree.month, date__day=daythree.day,
                                    user=request.user)
    foure = Exercise.objects.filter(date__year=dayfour.year, date__month=dayfour.month, date__day=dayfour.day,
                                   user=request.user)
    fivee = Exercise.objects.filter(date__year=dayfive.year, date__month=dayfive.month, date__day=dayfive.day,
                                   user=request.user)
    sixe = Exercise.objects.filter(date__year=daysix.year, date__month=daysix.month, date__day=daysix.day,
                                  user=request.user)
    sevene = Exercise.objects.filter(date__year=dayseven.year, date__month=dayseven.month, date__day=dayseven.day,
                                    user=request.user)

    caloriesonee = 0
    caloriestwoe = 0
    caloriesthreee = 0
    caloriesfoure = 0
    caloriesfivee = 0
    caloriessixe = 0
    caloriesevene = 0

    for exercise in onee:
        caloriesonee += exercise.calories_burned

    for exercise in twoe:
        caloriestwoe += exercise.calories_burned

    for exercise in threee:
        caloriesthreee += exercise.calories_burned

    for exercise in foure:
        caloriesfoure += exercise.calories_burned

    for exercise in fivee:
        caloriesfivee += exercise.calories_burned

    for exercise in sixe:
        caloriessixe += exercise.calories_burned

    for exercise in sevene:
        caloriesevene += exercise.calories_burned

    total_weekly_caloriese = caloriesonee + caloriestwoe + caloriesthreee + caloriesfoure + caloriesfivee + caloriessixe + caloriesevene

    total = Exercise.objects.filter(user=request.user)

    for exercise in total:
        total_caloriese += exercise.calories_burned

    caloriegoale = Goals.objects.get(pk=request.user.id).goal_calories_burned_per_day

    Weight.objects.get_or_create(pk=request.user.id)
    weights = Weight.objects.filter(user=request.user).order_by('date')

    weightamounts = []
    weightdates = []

    weightcurrent = weights.latest('date').weight
    goal, created = Goals.objects.get_or_create(pk=request.user.id)
    weightgoal = goal.goal_weight
    lbsleft = weightcurrent - weightgoal

    for weight in weights:
        weightamounts.append(weight.weight)
        weightdates.append(weight.date.strftime("%m-%d-%Y"))

    print(weightdates)
    print(weightamounts)

    context = {
        "title": "Dashboard",
        "pagename": "Dashboard",
        "total_calories": total_calories,
        "total_weekly_calories": total_weekly_calories,
        "dayone": dayone.strftime("%m-%d-%Y"),
        "daytwo": daytwo.strftime("%m-%d-%Y"),
        "daythree": daythree.strftime("%m-%d-%Y"),
        "dayfour": dayfour.strftime("%m-%d-%Y"),
        "dayfive": dayfive.strftime("%m-%d-%Y"),
        "daysix": daysix.strftime("%m-%d-%Y"),
        "dayseven": dayseven.strftime("%m-%d-%Y"),
        "caloriesone": caloriesone,
        "caloriestwo": caloriestwo,
        "caloriesthree": caloriesthree,
        "caloriesfour": caloriesfour,
        "caloriesfive": caloriesfive,
        "caloriessix": caloriessix,
        "calorieseven": calorieseven,
        "caloriegoal": caloriegoal,
        "total_caloriese": total_caloriese,
        "total_weekly_caloriese": total_weekly_caloriese,
        "caloriesonee": caloriesonee,
        "caloriestwoe": caloriestwoe,
        "caloriesthreee": caloriesthreee,
        "caloriesfoure": caloriesfoure,
        "caloriesfivee": caloriesfivee,
        "caloriessixe": caloriessixe,
        "caloriesevene": caloriesevene,
        "caloriegoale": caloriegoale,
        "weightcurrent": weightcurrent,
        "weightgoal": weightgoal,
        "lbsleft": lbsleft,
        "weightamounts": weightamounts,
        "weightdates": weightdates
    }
    return render(request, "weight/dashboard.html", context)


@login_required(login_url='login')
def calorietracking(request):
    total_calories = 0

    dayone = datetime.date.today()
    daytwo = datetime.date.today() - datetime.timedelta(days=1)
    daythree = datetime.date.today() - datetime.timedelta(days=2)
    dayfour = datetime.date.today() - datetime.timedelta(days=3)
    dayfive = datetime.date.today() - datetime.timedelta(days=4)
    daysix = datetime.date.today() - datetime.timedelta(days=5)
    dayseven = datetime.date.today() - datetime.timedelta(days=6)
    one = Food.objects.filter(date__year=dayone.year, date__month=dayone.month, date__day=dayone.day, user=request.user)
    two = Food.objects.filter(date__year=daytwo.year, date__month=daytwo.month, date__day=daytwo.day, user=request.user)
    three = Food.objects.filter(date__year=daythree.year, date__month=daythree.month, date__day=daythree.day, user=request.user)
    four = Food.objects.filter(date__year=dayfour.year, date__month=dayfour.month, date__day=dayfour.day, user=request.user)
    five = Food.objects.filter(date__year=dayfive.year, date__month=dayfive.month, date__day=dayfive.day, user=request.user)
    six = Food.objects.filter(date__year=daysix.year, date__month=daysix.month, date__day=daysix.day, user=request.user)
    seven = Food.objects.filter(date__year=dayseven.year, date__month=dayseven.month, date__day=dayseven.day, user=request.user)

    caloriesone = 0
    caloriestwo = 0
    caloriesthree = 0
    caloriesfour = 0
    caloriesfive = 0
    caloriessix = 0
    calorieseven = 0

    for food in one:
        caloriesone += food.calories_amount

    for food in two:
        caloriestwo += food.calories_amount

    for food in three:
        caloriesthree += food.calories_amount

    for food in four:
        caloriesfour += food.calories_amount

    for food in five:
        caloriesfive += food.calories_amount

    for food in six:
        caloriessix += food.calories_amount

    for food in seven:
        calorieseven += food.calories_amount

    total_weekly_calories = caloriesone + caloriestwo + caloriesthree + caloriesfour + caloriesfive + caloriessix + calorieseven

    total = Food.objects.filter(user=request.user)

    for food in total:
            total_calories += food.calories_amount

    caloriegoal = Goals.objects.get(pk=request.user.id).goal_calories_eaten_per_day

    context = {
        "title": "Calorie Tracking",
        "pagename": "Calorie Tracking",
        "total_calories": total_calories,
        "total_weekly_calories": total_weekly_calories,
        "dayone": dayone.strftime("%m-%d-%Y"),
        "daytwo": daytwo.strftime("%m-%d-%Y"),
        "daythree": daythree.strftime("%m-%d-%Y"),
        "dayfour": dayfour.strftime("%m-%d-%Y"),
        "dayfive": dayfive.strftime("%m-%d-%Y"),
        "daysix": daysix.strftime("%m-%d-%Y"),
        "dayseven": dayseven.strftime("%m-%d-%Y"),
        "caloriesone": caloriesone,
        "caloriestwo": caloriestwo,
        "caloriesthree": caloriesthree,
        "caloriesfour": caloriesfour,
        "caloriesfive": caloriesfive,
        "caloriessix": caloriessix,
        "calorieseven": calorieseven,
        "caloriegoal": caloriegoal
    }

    return render(request, "weight/calories.html", context)


@login_required(login_url='login')
def exercisetracking(request):
    total_calories = 0

    dayone = datetime.date.today()
    daytwo = datetime.date.today() - datetime.timedelta(days=1)
    daythree = datetime.date.today() - datetime.timedelta(days=2)
    dayfour = datetime.date.today() - datetime.timedelta(days=3)
    dayfive = datetime.date.today() - datetime.timedelta(days=4)
    daysix = datetime.date.today() - datetime.timedelta(days=5)
    dayseven = datetime.date.today() - datetime.timedelta(days=6)
    one = Exercise.objects.filter(date__year=dayone.year, date__month=dayone.month, date__day=dayone.day, user=request.user)
    two = Exercise.objects.filter(date__year=daytwo.year, date__month=daytwo.month, date__day=daytwo.day, user=request.user)
    three = Exercise.objects.filter(date__year=daythree.year, date__month=daythree.month, date__day=daythree.day,
                                user=request.user)
    four = Exercise.objects.filter(date__year=dayfour.year, date__month=dayfour.month, date__day=dayfour.day,
                               user=request.user)
    five = Exercise.objects.filter(date__year=dayfive.year, date__month=dayfive.month, date__day=dayfive.day,
                               user=request.user)
    six = Exercise.objects.filter(date__year=daysix.year, date__month=daysix.month, date__day=daysix.day, user=request.user)
    seven = Exercise.objects.filter(date__year=dayseven.year, date__month=dayseven.month, date__day=dayseven.day,
                                user=request.user)

    caloriesone = 0
    caloriestwo = 0
    caloriesthree = 0
    caloriesfour = 0
    caloriesfive = 0
    caloriessix = 0
    calorieseven = 0

    for exercise in one:
        caloriesone += exercise.calories_burned

    for exercise in two:
        caloriestwo += exercise.calories_burned

    for exercise in three:
        caloriesthree += exercise.calories_burned

    for exercise in four:
        caloriesfour += exercise.calories_burned

    for exercise in five:
        caloriesfive += exercise.calories_burned

    for exercise in six:
        caloriessix += exercise.calories_burned

    for exercise in seven:
        calorieseven += exercise.calories_burned

    total_weekly_calories = caloriesone + caloriestwo + caloriesthree + caloriesfour + caloriesfive + caloriessix + calorieseven

    total = Exercise.objects.filter(user=request.user)

    for exercise in total:
            total_calories += exercise.calories_burned

    caloriegoal = Goals.objects.get(pk=request.user.id).goal_calories_burned_per_day

    context = {
        "title": "Exercise Tracking",
        "pagename": "Exercise Tracking",
        "total_calories": total_calories,
        "total_weekly_calories": total_weekly_calories,
        "dayone": dayone.strftime("%m-%d-%Y"),
        "daytwo": daytwo.strftime("%m-%d-%Y"),
        "daythree": daythree.strftime("%m-%d-%Y"),
        "dayfour": dayfour.strftime("%m-%d-%Y"),
        "dayfive": dayfive.strftime("%m-%d-%Y"),
        "daysix": daysix.strftime("%m-%d-%Y"),
        "dayseven": dayseven.strftime("%m-%d-%Y"),
        "caloriesone": caloriesone,
        "caloriestwo": caloriestwo,
        "caloriesthree": caloriesthree,
        "caloriesfour": caloriesfour,
        "caloriesfive": caloriesfive,
        "caloriessix": caloriessix,
        "calorieseven": calorieseven,
        "caloriegoal": caloriegoal
    }

    return render(request, "weight/exercise.html", context)


@login_required(login_url='login')
def goals(request, pk):
    usergoal, created = Goals.objects.get_or_create(pk=pk)
    form = UpdateGoal(instance=usergoal)

    if request.method == "POST":
        form = UpdateGoal(request.POST, instance=usergoal)
        if form.is_valid():
            form.save()
            return redirect("weight-goals", pk)
    return render(request, "weight/goals.html", {"title": "Goals", "pagename": "Goals", "form": form})


@login_required(login_url='login')
def tracking(request):
    Weight.objects.get_or_create(pk=request.user.id)
    weights = Weight.objects.filter(user=request.user).order_by('date')

    weightamounts = []
    weightdates = []

    weightcurrent = weights.latest('date').weight
    goal, created = Goals.objects.get_or_create(pk=request.user.id)
    weightgoal = goal.goal_weight
    lbsleft = weightcurrent - weightgoal

    for weight in weights:
        weightamounts.append(weight.weight)
        weightdates.append(weight.date.strftime("%m-%d-%Y"))

    context = {
        "title": "Weight Tracking",
        "pagename": "Weight Tracking",
        "weightcurrent": weightcurrent,
        "weightgoal": weightgoal,
        "lbsleft": lbsleft,
        "weightamounts": weightamounts,
        "weightdates": weightdates
    }
    return render(request, "weight/trackweight.html", context)


@login_required(login_url='login')
def add_food(request):
    form = CreateFoodItem()
    if request.method == "POST":
        form = CreateFoodItem(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect("weight-calories")
    return render(request, "weight/add_food.html", {"title": "Add Food", "form": form})


@login_required(login_url='login')
def view_food(request):
    foodlist = Food.objects.filter(user=request.user)
    return render(request, "weight/food_history.html", {"title": "View Food History", "pagename": "Your Food History", "foodlist": foodlist})


@login_required(login_url='login')
def update_food(request, pk):
    food = Food.objects.get(pk=pk)
    form = CreateFoodItem(instance=food)

    if request.method == "POST":
        form = CreateFoodItem(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect("weight-view-food")
    return render(request, "weight/update_food.html", {"title": "Update Food", "pagename": "Update Food Item", "form": form})


@login_required(login_url='login')
def delete_food(request, pk):
    food = Food.objects.get(pk=pk)

    if request.method == "POST":
        food.delete()
        return redirect("weight-view-food")

    return render(request, "weight/delete_food.html", {"title": "Delete Food Item", "pagename": "Delete Food Item", "food": food})


@login_required(login_url='login')
def view_exercise(request):
    exerciselist = Exercise.objects.filter(user=request.user)
    return render(request, "weight/exercise_history.html", {"title": "View Exercise History", "pagename": "Your Exercise History", "exerciselist": exerciselist})


@login_required(login_url='login')
def add_exercise(request):
    form = CreateExercise()
    if request.method == "POST":
        form = CreateExercise(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            return redirect("weight-exercise")
    return render(request, "weight/add_exercise.html", {"title": "Add Exercise", "form": form})


@login_required(login_url='login')
def update_exercise(request, pk):
    exercise = Exercise.objects.get(pk=pk)
    form = CreateExercise(instance=exercise)

    if request.method == "POST":
        form = CreateExercise(request.POST, instance=exercise)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            return redirect("weight-view-exercise")
    return render(request, "weight/update_exercise.html", {"title": "Update Exercise", "pagename": "Update Exercise", "form": form})

@login_required(login_url='login')
def delete_exercise(request, pk):
    exercise = Exercise.objects.get(pk=pk)

    if request.method == "POST":
        exercise.delete()
        return redirect("weight-view-exercise")

    return render(request, "weight/delete_exercise.html", {"title": "Delete Exercise", "pagename": "Delete Exercise", "exercise": exercise})

@login_required(login_url='login')
def view_weight(request):
    weightlist = Weight.objects.filter(user=request.user)
    return render(request, "weight/weight_history.html", {"title": "View Weight History", "pagename": "Your Weight History", "weightlist": weightlist})


@login_required(login_url='login')
def add_weight(request):
    form = CreateWeight()
    if request.method == "POST":
        form = CreateWeight(request.POST)
        if form.is_valid():
            weight = form.save(commit=False)
            weight.user = request.user
            weight.save()
            return redirect("weight-tracking")
    return render(request, "weight/add_weight.html", {"title": "Add weight", "form": form})


@login_required(login_url='login')
def update_weight(request, pk):
    weight = Weight.objects.get(pk=pk)
    form = CreateWeight(instance=weight)

    if request.method == "POST":
        form = CreateWeight(request.POST, instance=weight)
        if form.is_valid():
            weight = form.save(commit=False)
            weight.user = request.user
            weight.save()
            return redirect("weight-view-weight")
    return render(request, "weight/update_weight.html", {"title": "Update weight", "pagename": "Update weight", "form": form})

@login_required(login_url='login')
def delete_weight(request, pk):
    weight = Weight.objects.get(pk=pk)

    if request.method == "POST":
        weight.delete()
        return redirect("weight-view-weight")

    return render(request, "weight/delete_weight.html", {"title": "Delete Weight", "pagename": "Delete Weight", "weight": weight})
