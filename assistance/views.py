from django.shortcuts import render, redirect, get_object_or_404
from .models import AssistanceRequest, AssistanceResponse
from .forms import AssistanceRequestForm, AssistanceResponseForm
from django.core.mail import send_mail

def assistance_responses(request, request_id):
    responses = AssistanceResponse.objects.filter(request_id=request_id)
    return render(request, 'assistance/assistance_responses.html', {'responses': responses})

def request_assistance(request, mechanic_id):
    if request.method == 'POST':
        form = AssistanceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            assistance_request = form.save(commit=False)
            assistance_request.user = request.user
            assistance_request.mechanic_id = mechanic_id  
            assistance_request.save()

            subject = 'New Assistance Request'
            message = 'A new assistance request has been made. Please check your dashboard for more details.'
            from_email = 'admin@cloud.skillfam.com'
            recipient_list = [assistance_request.mechanic.user.email]
            send_mail(subject, message, from_email, recipient_list)
                
            return redirect('home')  
    else:
        form = AssistanceRequestForm()
    return render(request, 'assistance/request_assistance.html', {'form': form})


def respond_to_request(request, request_id):
    assistance_request = get_object_or_404(AssistanceRequest, id=request_id)
    
    if request.method == 'POST':
        form = AssistanceResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.request = assistance_request
            response.mechanic = request.user.mechanic 
            response.save()
             
            subject = 'New Assistance Response'
            message = 'A new assistance response has been made. Please check your dashboard for more details.'
            from_email = 'admin@cloud.skillfam.com'
            recipient_list = [assistance_request.user.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('mechanic_dashboard') 
       
    else:
        form = AssistanceResponseForm()
    
    return render(request, 'assistance/assistance_response.html', {'form': form, 'assistance_request': assistance_request})