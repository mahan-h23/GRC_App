from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Corporate CRUD

def createCorporate(request):
    context = {}
    form = CorprateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listcorpo')

    context['form'] = form

    return render(request, 'information/corprate/create.html', context)


def listCorporate(request):
    context = {}
    corporate = CorprateObjective.objects.filter(flag=True)
    context['corpo'] = corporate

    return render(request, 'information/corprate/list.html', context)


def deleteCorporate(request, pk):
    context = {}
    corpo = CorprateObjective.objects.get(id=pk)
    corponame = corpo.name

    if request.method == "POST":
        CorprateObjective.objects.filter(id=pk).update(flag=False)
        return redirect('listcorpo')
    context['corpo']=corponame

    return render(request, 'information/corprate/delete.html', context)






def updateCorporate(request, pk):
    context = {}
    corpo = CorprateObjective.objects.get(id=pk)
    form = CorprateForm(request.POST or None, instance=corpo)

    if form.is_valid():
        form.save()
        return redirect('listcorpo')

    context['form'] = form
    return render(request, 'information/corprate/update.html', context)


def detailCorporate(request,pk):
    context = {}
    corpo = CorprateObjective.objects.filter(id=pk).filter(flag=True)
    context['corpo']=corpo

    return render(request,'information/corprate/detail.html',context)

