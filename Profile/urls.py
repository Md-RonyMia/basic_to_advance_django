from django.urls import path
from . import views

urlpatterns = [
    path('add_profile',views.ProfileView,name='profile')

]