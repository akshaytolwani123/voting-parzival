from django.urls import path
from . import views
from .models import Captain
id = Captain.id
app_name = 'captain'
urlpatterns = [
    path('', views.captain_view, name = 'captains'),
    path('<int:id>', views.vote, name = 'vote')
]