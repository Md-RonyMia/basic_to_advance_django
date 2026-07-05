from django.urls import path
from . import views

urlpatterns = [
    path('courses/',views.Courses),
    path('about/page/<int:i_d>/',views.About,name='home'),
    path('index/',views.Index),
]
