from django.urls import path
from . import views

urlpatterns = [
       path('add_post/',views.PostView,name='post'),
       path('edit/<int:id>',views.edit_post,name='edit'),
       path('delete/<int:id>',views.delete_post,name='delete')

]