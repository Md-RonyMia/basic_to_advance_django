from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.Courses),
    path('about/', views.About, name='home'),
    path('index/', views.Index),
    path('form/',views.user_form,name='userform'),
    path('django_form/',views.Django_form,name='django_form')
]
