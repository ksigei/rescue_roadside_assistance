from django.shortcuts import render
from mechanics.models import Mechanic
from motorist.models import Motorist

def home(request):
    if request.user.is_authenticated:
        try:
            mechanic = Mechanic.objects.get(user=request.user)
            context = {'mechanic': mechanic}
        except Mechanic.DoesNotExist:
            mechanic = None
        
        try:
            motorist = Motorist.objects.get(user=request.user)
            context = {'motorist': motorist}
        except Motorist.DoesNotExist:
            motorist = None

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
