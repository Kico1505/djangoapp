from django.urls import path
from . import views
from users import views as user_views
urlpatterns = [
    path('', views.dashboard, name='weight-dashboard'),
    path('calories/', views.calorietracking, name='weight-calories'),
    path('exercise/', views.exercisetracking, name='weight-exercise'),
    path('goals/<str:pk>/', views.goals, name='weight-goals'),
    path('tracking/', views.tracking, name='weight-tracking'),
    path('profile/', user_views.profile, name='weight-profile'),
    path('add-food/', views.add_food, name='weight-add-food'),
    path('view-food/', views.view_food, name='weight-view-food'),
    path('update-food/<str:pk>/', views.update_food, name='weight-update-food'),
    path('delete-food/<str:pk>/', views.delete_food, name='weight-delete-food'),
    path('add-exercise/', views.add_exercise, name='weight-add-exercise'),
    path('view-exercise/', views.view_exercise, name='weight-view-exercise'),
    path('update-exercise/<str:pk>', views.update_exercise, name='weight-update-exercise'),
    path('delete-exercise/<str:pk>', views.delete_exercise, name='weight-delete-exercise'),
    path('add-weight/', views.add_weight, name='weight-add-weight'),
    path('view-weight/', views.view_weight, name='weight-view-weight'),
    path('update-weight/<str:pk>', views.update_weight, name='weight-update-weight'),
    path('delete-weight/<str:pk>', views.delete_weight, name='weight-delete-weight')
]
