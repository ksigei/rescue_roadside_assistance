from django.shortcuts import render, redirect
from .models import Motorist
from .forms import MotoristProfileForm

def update_motorist_profile(request):
    motorist = Motorist.objects.get(user=request.user)
    if request.method == 'POST':
        form = MotoristProfileForm(request.POST, request.FILES, instance=motorist)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = MotoristProfileForm(instance=motorist)
    return render(request, 'profile/update_profile.html', {'form': form})