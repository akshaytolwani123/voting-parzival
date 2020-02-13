from django.shortcuts import render

def home_view(reuqest):
    return render(reuqest, 'home.html')

