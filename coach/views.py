from django.shortcuts import render,redirect
from django.http import HttpResponse
# from supplier.models import Sup_verify,New_sup

def dashboard(request):
    return render(request,'coach/dashboard.html')

def profile(request):
    return render(request,'coach/profile.html')

def upcoming(request):
    return render(request,'coach/upcoming.html')

def history(request):
    return render(request,'coach/callhistory.html')

def availability(request):
    return render(request,'coach/avail.html')

