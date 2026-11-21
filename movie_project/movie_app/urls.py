from django.urls import path
from . import views

urlpatterns = [
    path('lookups/', views.movie_lookups, name='movie_lookups'),
]
