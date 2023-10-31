from django.urls import path

from olympiads.views import *
urlpatterns = [
    path('', index),
    path('people/<int:peopleid>/', categories)
]