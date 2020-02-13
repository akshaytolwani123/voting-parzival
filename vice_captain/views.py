from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Vice_Captain
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = '/account')
def vice_captain(request):
    user = User.objects.get(id = request.user.id)
    vice_captains = Vice_Captain.objects.all()
    return render(request, 'vice_captain/vote.html', {'vice_captains': vice_captains, 'user': user})

def vote(request, id):
    user = User.objects.get(id=request.user.id)
    if User.profile.has_voted_for_vice_captain == True:
        return redirect('/')
    else:
        vice_captain = Vice_Captain.objects.get(id=id)
        vice_captain.votes += 1
        user.profile.has_voted_for_vice_captain = True
        user.profile.voted_captain = captain.name
        user.save()
        del captain, user
        return redirect('/')
