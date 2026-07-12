from django.urls import path
from . import views

urlpatterns = [
    path('add_author',views.authorview,name='add_author')

]