from django.urls import path
from . views import view_list , create_view , view_individual , update_view , delete_view

urlpatterns = [
    path('' , view_list , name='view_list'),
    path('create/' , create_view , name='create_view'),
    path('<int:pk>/' , view_individual , name='view_individual'),
    path('<int:pk>/edit/' , update_view , name='update_view'),
    path('<int:pk>/delete/' , delete_view , name='delete_view')
]