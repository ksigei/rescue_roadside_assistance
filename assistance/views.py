# views.py

from django.shortcuts import render, redirect
from .models import AssistanceRequest
from .forms import AssistanceRequestForm

def request_assistance(request, mechanic_id):
    if request.method == 'POST':
        form = AssistanceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            assistance_request = form.save(commit=False)
            assistance_request.user = request.user
            assistance_request.mechanic_id = mechanic_id  # Set the mechanic ID
            assistance_request.save()
            return redirect('home')  # Redirect to the home page or any other page
    else:
        form = AssistanceRequestForm()
    return render(request, 'assistance/request_assistance.html', {'form': form})
