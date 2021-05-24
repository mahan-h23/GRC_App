from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import *




@login_required(login_url='account/log')
def viewdash(request):
    context = {}
    profilepic = ProfileInfo.objects.all()
    context['pics'] = profilepic
    context['nbar'] = 'dashboard'



    return render(request,'examples/dashboard.html',context)

def testView(request):
    return render(request,'main/dashboard.html')

def techview(request):
    return render(request,'division/tech.html')


def marketingview(request):
    return render(request,'division/arketing.html')


def bdview(request):
    return render(request,'division/bd.html')

def financeview(request):
    return render(request,'division/finance.html')


def operationview(request):
    return render(request,'division/operation.html')


def legalview(request):
    return render(request,'division/legal.html')


def hrview(request):
    return render(request,'division/hr.html')

def coomercial(request):
    return render(request,'division/commercial.html')

def cxview(request):
    return render(request,'division/cx.html')


def crossview(request):
    return render(request,'division/cross.html')


def viewDashboard(request):
    context = {}
    context['nbar'] = 'dashboard'
    return render(request,'main/dashboard.html',context)