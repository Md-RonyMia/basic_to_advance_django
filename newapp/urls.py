from django.urls import path
from . import views

urlpatterns = [
    path('courses/',views.Courses),
    path('about/',views.About),
    path('index/',views.Index),
]
