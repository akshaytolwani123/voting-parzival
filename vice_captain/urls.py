from django.urls import path
from . import views
from .models import Vice_Captain
app_name = 'vice_captain'
id = Vice_Captain.id
urlpatterns = [
    path('', views.vice_captain, name = 'vice_captain'),
    path('<int:id>/', views.vote, name='vote')

]