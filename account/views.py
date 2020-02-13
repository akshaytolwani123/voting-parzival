from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            return render(request, 'account/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})
