from django.urls import path

from .views import TeamsView
urlpatterns = [
   path('', TeamsView, name='team'),
]