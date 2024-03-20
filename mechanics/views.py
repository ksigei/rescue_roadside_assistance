from django.shortcuts import render, redirect
from .models import Mechanic
from .forms import MechanicProfileForm

def update_mechanic_profile(request):
    mechanic = Mechanic.objects.get(user=request.user)
    if request.method == 'POST':
        form = MechanicProfileForm(request.POST, request.FILES, instance=mechanic)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = MechanicProfileForm(instance=mechanic)
    return render(request, 'profile/update_profile.html', {'form': form})