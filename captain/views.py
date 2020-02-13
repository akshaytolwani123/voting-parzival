from django.shortcuts import render, redirect
from .models import Captain
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = '/account/')
def captain_view(request):
    user = User.objects.get(id = request.user.id)
    captain = Captain.objects.all()
    return render(request, 'captain/vote.html', {'captains': captain, 'user': user})

def vote(request, id):
    user = User.objects.get(id=request.user.id)
    if user.profile.has_voted_for_captain == True:
        return render(request, 'captain/vote.html', {'captains': captain, 'user': user})

    else:
        captain = Captain.objects.get(id = id)
        captain.votes += 1
        user.profile.has_voted_for_captain = True
        user.profile.voted_captain = captain.name
        user.save()
        del captain, user
        return redirect('/')
