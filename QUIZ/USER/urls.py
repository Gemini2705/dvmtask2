from django.urls import path, include
from . import views as user_views



urlpatterns = [
    path('', user_views.dashboard, name='dashboard'),
    path('quiz/<str:quizname>/', include('registration.urls') ),    
    path('result/<str:quizname>/', user_views.resultPG, name='result'),


     

]