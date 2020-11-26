from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
import datetime
from customer.models import New_cust

def index(request):
    # return redirect('/index/')
    return render(request,'reschedule.html')

def page(request,pagge):
    a = pagge+'.html'
    return render(request,a )

def course(request):
    if request.session.get('cust_id'):
        return render(request,'course.html')
    else:
        return redirect('/index/')

def course_details(request):
    if request.session.get('cust_id'):
        return render(request,'course_details.html')
    else:
        return redirect('/index/')

class aftersignup(View):
    def get(self,request):
        return redirect('/index/')
    
    def post(self,request):
        data = {
        'cust_name' : request.POST.get('name'),
        'cust_mail' : request.POST.get('email'),
        'cust_phone' : request.POST.get('mobile'),
        'cust_pswd' : request.POST.get('pass'),
        }
        if New_cust.objects.filter(cust_mail=data['cust_mail']).exists() or New_cust.objects.filter(cust_phone=data['cust_phone']).exists():
            return redirect('/Sigin/')
        else:
            data['cust_id'] = 'Customer-'+data['cust_phone']
            obj = New_cust.objects.create(**data)
            obj.save()
            request.session['data'] = data
            return redirect('/Sigin/')

def aftersignin(request):
    cust_mail = request.POST.get('email')
    cust_pswd = request.POST.get('pass')
    print(cust_mail)
    try:
        if '@' in cust_mail:
            obj = New_cust.objects.get(cust_mail=cust_mail)
        else:
            obj = New_cust.objects.get(cust_phone=cust_mail)
            print(cust_mail,obj)
    except:
        return redirect('/index/')
    else:
        if cust_pswd == obj.cust_pswd:
            request.session['cust_id'] = obj.cust_id
            return redirect('/coach/')
        else:
            return redirect('/')

def logout(request):
    if request.session.get('cust_id'):
        del request.session['cust_id']
        return redirect('/Sigin/')
    else:
        return redirect('/index/')