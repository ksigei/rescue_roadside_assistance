from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from motorist.models import Motorist
from mechanics.models import Mechanic

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            if role == 'motorist':
                Motorist.objects.create(user=user)
                login(request, user)
                return redirect('update_motorist_profile')  # Redirect to motorist profile update view
            elif role == 'mechanic':
                Mechanic.objects.create(user=user)
                login(request, user)
                return redirect('update_mechanic_profile')  # Redirect to mechanic profile update view
            login(request, user)
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})