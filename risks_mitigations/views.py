from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.utils.encoding import smart_str

from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse

import csv


def riskView(request):
    contex = {}
    risks = Risk.objects.all()

    form = RiskForm(request.POST or None, initial={'createdBy': request.user})

    if form.is_valid():
        form.save()
        riskid = Risk.objects.last()
        return redirect('mitigation', pk=riskid.id)

    contex['form'] = form
    contex['risks'] = risks

    return render(request, 'riskadd/addrisk.html', contex)


def mitigationView(request, pk):
    context = {}
    risk = Risk.objects.get(id=pk)
    form = MitigationForm(request.POST or None, initial={'risk': risk, 'dueDate': timezone.now()})

    if request.POST:
        if 'btn1' in request.POST and form.is_valid():
            form.save()
            return redirect('dash')
        elif 'btn2' in request.POST and form.is_valid():
            form.save()

    context['risk'] = risk
    context['form'] = form

    return render(request, 'riskadd/mitigationadd.html', context)


def test(request):
    return render(request, 'riskadd/index.html')


def riskDetail(request, pk):
    context = {}
    mitigation_detail = Mitigation.objects.filter(risk_id=pk).values_list('mitigation', 'dueDate')
    risk_detail = Risk.objects.get(id=pk)

    qid = Risk.objects.get(id=pk)
    context['mitigation'] = mitigation_detail
    context['risk'] = risk_detail
    context['qid'] = qid.id

    return render(request, 'riskadd/riskdetail.html', context)


# Test query
def sqlq(request, pk):
    contex = {}
    myrisk = Risk.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)

    queryset = Mitigation.objects.filter(risk_id=pk).values_list('risk_id', 'mitigation', 'risk__createdBy',
                                                                 'risk__riskname')
    qid = Risk.objects.get(id=pk)
    for field in queryset:
        writer.writerow(field)
    contex['risks'] = queryset
    contex['qid'] = qid.id
    contex['csv'] = writer

    return render(request, 'riskadd/query.html', contex)


# def for downloading excel file

def grtfile(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Risk Assessment.csv"'
    writer = csv.writer(response)
    writer.writerow([
        smart_str(u"Event Name"),
        smart_str(u"Start Date"),
        smart_str(u"End Date"),

    ])

    queryset = Mitigation.objects.filter(risk_id=pk).values_list('mitigation', 'risk__createdBy', 'risk__riskname')

    for field in queryset:
        writer.writerow(field)

    return response


def riskUpdate(request,pk):
    context = {}
    obj = Risk.objects.get(id=pk)
    form = RiskForm(request.POST or None, instance=obj)
    getStr = str(pk)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/add/detail/'+getStr)

    context['form'] = form

    return render(request,'riskadd/riskupdate.html',context)