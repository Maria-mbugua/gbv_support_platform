from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import GBVCenter, Message, IncidentReport
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful. Welcome!')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please try logging in.')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful. Welcome back!')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please check your credentials.')
        else:
            messages.error(request, 'Login failed. Please correct the errors below.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    centers = GBVCenter.objects.all()
    return render(request, 'home.html', {'centers': centers})

def send_message(request):
    if request.method == 'POST':
        content = request.POST['content']
        anonymous = request.POST.get('anonymous', False)
        user = None if anonymous else request.user
        Message.objects.create(user=user, anonymous=anonymous, content=content)
        messages.success(request, 'Message sent successfully.')
        return redirect('home')
    return render(request, 'send_message.html')

def report_incident(request):
    if request.method == 'POST':
        description = request.POST['incident']
        user = request.user if request.user.is_authenticated else None
        IncidentReport.objects.create(user=user, description=description)
        messages.success(request, 'Incident reported successfully.')
        return redirect('home')
    return render(request, 'report_incident.html')

@login_required
def view_incidents(request):
    if request.user.is_superuser:
        incidents = IncidentReport.objects.all()
        return render(request, 'view_incidents.html', {'incidents': incidents})
    else:
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')

@staff_member_required
def review_incidents(request):
    pending_incidents = IncidentReport.objects.filter(status='Pending')
    reviewed_incidents = IncidentReport.objects.filter(status='Reviewed')
    return render(request, 'review_incidents.html', {'pending_incidents': pending_incidents, 'reviewed_incidents': reviewed_incidents})

@staff_member_required
def update_incident(request, incident_id):
    incident = IncidentReport.objects.get(id=incident_id)
    if request.method == 'POST':
        incident.status = 'Reviewed'
        incident.recommendation = request.POST['recommendation']
        incident.save()
        messages.success(request, 'Incident updated successfully.')
        return redirect('review_incidents')
    return render(request, 'update_incident.html', {'incident': incident})

def resource1(request):
    return render(request, 'resource1.html')

def resource2(request):
    return render(request, 'resource2.html')

def resource3(request):
    return render(request, 'resource3.html')

def resource4(request):
    return render(request, 'resource4.html')

def resource5(request):
    return render(request, 'resource5.html')

def story1(request):
    return render(request, 'story1.html')

def story2(request):
    return render(request, 'story2.html')

def story3(request):
    return render(request, 'story3.html')









