from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('add_note',add_note,name='add_note'),
    path('delete_note/<int:my_id>/',delete_note,name='delete_note'),
    path('edit_note/<int:my_id>/',edit_note,name='edit_note'),
    path('update_note/<int:my_id>/',update_note,name='update_note'),
]
