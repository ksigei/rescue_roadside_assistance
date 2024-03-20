from django.shortcuts import render, redirect, get_object_or_404
from .models import Mechanic
from .forms import MechanicProfileForm

def mechanic_list(request):
    mechanics = Mechanic.objects.all()
    # Filter
    query = request.GET.get('q')
    specialization = request.GET.get('specialization')

    if query:
        mechanics = mechanics.filter(user__username__icontains=query)
    if specialization:
        mechanics = mechanics.filter(specializations=specialization)

    context = {
        'mechanics': mechanics,
    }
    return render(request, 'mechanic_list.html', context)

def mechanic_detail(request, mechanic_id):
    mechanic = get_object_or_404(Mechanic, pk=mechanic_id)
    return render(request, 'mechanic_detail.html', {'mechanic': mechanic})

def mechanic_profile(request, mechanic_id):
    mechanic = get_object_or_404(Mechanic, id=mechanic_id)
    return render(request, 'profile/mechanic_profile.html', {'mechanic': mechanic})

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