from django.urls import path
from USER import views as user_views

urlpatterns = [
    path('', user_views.quiz, name='dashboard'),
        
    path('result/<str:quizname>', user_views.resultPG, name='result'),


 ]