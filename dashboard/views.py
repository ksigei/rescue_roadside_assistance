from django.shortcuts import render
from mechanics.models import Mechanic
from motorist.models import Motorist
from assistance.models import AssistanceRequest, AssistanceResponse

def mechanic_dashboard(request):
    mechanic = Mechanic.objects.get(user=request.user)
    assistance_requests = AssistanceRequest.objects.filter(mechanic=mechanic)
    assistance_responses = AssistanceResponse.objects.filter(mechanic=mechanic)
    return render(request, 'dashboard/mechanic_dashboard.html', {'mechanic': mechanic, 'assistance_requests': assistance_requests, 'assistance_responses': assistance_responses})

def motorist_dashboard(request):
    motorist = Motorist.objects.get(user=request.user)
    assistance_requests = AssistanceRequest.objects.filter(user=motorist.user)
    # assistance_responses = AssistanceResponse.objects.filter(assistance = assistance_requests)
    return render(request, 'dashboard/motorist_dashboard.html', {'motorist': motorist, 'assistance_requests': assistance_requests})
