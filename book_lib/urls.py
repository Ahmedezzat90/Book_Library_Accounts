from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_book,name='all_book' ),
    path('add_book',views.add_book,name='add_book' ),
    path('edit_book/<str:slug>/',views.edit_book,name='edit_book' ),
    path('delete_book/<str:slug>/',views.delete_book,name='delete_book' ),
    path('show_details/<str:slug>/',views.show_details,name='show_details' ),


]