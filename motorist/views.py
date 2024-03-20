from django.shortcuts import render, redirect, get_object_or_404
from .models import Motorist
from .forms import MotoristProfileForm

def motorist_profile(request, motorist_id):
    motorist = get_object_or_404(Motorist, id=motorist_id)
    return render(request, 'profile/motorist_profile.html', {'motorist': motorist})

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