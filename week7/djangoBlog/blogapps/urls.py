from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:game_id>', detail, name='detail'),
    path('create/', create, name='create'),
    path('comment/<str:game_id>/', comment, name='comment'),

    path('edit/<str:game_id>/', edit, name='edit'),
    path('update/<str:game_id>/', update, name='update'),
    path('delete/<str:game_id>', delete, name='delete'),
]