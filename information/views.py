from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.utils.translation import ugettext_lazy as _


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
    context['corpo'] = corponame

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


def detailCorporate(request, pk):
    context = {}
    corpo = CorprateObjective.objects.filter(id=pk, flag=True)
    context['corpo'] = corpo

    return render(request, 'information/corprate/detail.html', context)


# ---------------------------------------------------------------------------


# Division CRUD

def createDivision(request):
    context = {}
    form = DivisionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listdivision')

    context['form'] = form

    return render(request, 'information/division/create.html', context)


def listDivision(request):
    context = {}
    division = Division.objects.filter(flag=True)
    context['division'] = division

    return render(request, 'information/division/list.html', context)


def deleteDivision(request, pk):
    context = {}
    division = Division.objects.get(id=pk)
    divisionName = division.division

    if request.method == "POST":
        Division.objects.filter(id=pk).update(flag=False)
        return redirect('listdivision')
    context['division'] = divisionName

    return render(request, 'information/division/delete.html', context)


def updateDivision(request, pk):
    context = {}
    division = Division.objects.get(id=pk)
    form = DivisionForm(request.POST or None, instance=division)

    if form.is_valid():
        form.save()
        return redirect('listdivision')

    context['form'] = form
    return render(request, 'information/division/update.html', context)


def detailDivision(request, pk):
    context = {}
    division = Division.objects.filter(id=pk, flag=True)
    context['division'] = division

    return render(request, 'information/division/detail.html', context)


# --------------------------------------------------------------------------

# Owner CRUD

def createOwner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listowner')

    context['form'] = form

    return render(request, 'information/owner/create.html', context)


def listOwner(request):
    context = {}
    owner = Owners.objects.filter(flag=True)
    context['owner'] = owner

    return render(request, 'information/owner/list.html', context)


def deleteOwner(request, pk):
    context = {}
    owner = Owners.objects.get(id=pk)
    ownerName = owner.last_name

    if request.method == "POST":
        Owners.objects.filter(id=pk).update(flag=False)
        return redirect('listowner')
    context['owner'] = ownerName

    return render(request, 'information/owner/delete.html', context)


def updateOwner(request, pk):
    context = {}
    owner = Owners.objects.get(id=pk)
    form = OwnerForm(request.POST or None, instance=owner)

    if form.is_valid():
        form.save()
        return redirect('listowner')

    context['form'] = form
    return render(request, 'information/owner/update.html', context)


def detailOwner(request, pk):
    context = {}
    owner = Owners.objects.filter(id=pk, flag=True)
    context['owner'] = owner

    return render(request, 'information/owner/detail.html', context)


# --------------------------------------------------------------------------

# Biz KPI CRUD

def createBiz(request):
    context = {}
    form = BizKpiForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listbiz')

    context['form'] = form

    return render(request, 'information/bizkpi/create.html', context)


def listBiz(request):
    context = {}
    biz = BizKPI.objects.filter(flag=True)
    context['biz'] = biz

    return render(request, 'information/bizkpi/list.html', context)


def deleteBiz(request, pk):
    context = {}
    biz = BizKPI.objects.get(id=pk)
    bizName = biz

    if request.method == "POST":
        BizKPI.objects.filter(id=pk).update(flag=False)
        return redirect('listbiz')
    context['biz'] = bizName

    return render(request, 'information/bizkpi/delete.html', context)


def updateBiz(request, pk):
    context = {}
    biz = BizKPI.objects.get(id=pk)
    form = BizKpiForm(request.POST or None, instance=biz)

    if form.is_valid():
        form.save()
        return redirect('listbiz')

    context['form'] = form
    return render(request, 'information/bizkpi/update.html', context)


def detailBiz(request, pk):
    context = {}
    biz = BizKPI.objects.filter(id=pk, flag=True)
    context['biz'] = biz

    return render(request, 'information/bizkpi/detail.html', context)


# -----------------------------------------------------------------------------

# Principal risk CRUD

def createPrincipal(request):
    context = {}
    form = PrincipalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listprincipal')

    context['form'] = form

    return render(request, 'information/principal/create.html', context)


def listPrincipal(request):
    context = {}
    principal = PrincipalRisk.objects.filter(flag=True)
    context['principal'] = principal

    return render(request, 'information/principal/list.html', context)


def deletePrincipal(request, pk):
    context = {}
    principal = PrincipalRisk.objects.get(id=pk)
    principalName = principal.prShortTitile

    if request.method == "POST":
        PrincipalRisk.objects.filter(id=pk).update(flag=False)
        return redirect('listprincipal')
    context['principal'] = principalName

    return render(request, 'information/principal/delete.html', context)


def updatePrincipal(request, pk):
    context = {}
    principal = PrincipalRisk.objects.get(id=pk)
    form = PrincipalForm(request.POST or None, instance=principal)

    if form.is_valid():
        form.save()
        return redirect('listprincipal')

    context['form'] = form
    return render(request, 'information/principal/update.html', context)


def detailPrincipal(request, pk):
    context = {}
    principal = PrincipalRisk.objects.filter(id=pk, flag=True)
    context['principal'] = principal

    return render(request, 'information/principal/detail.html', context)


# --------------------------------------------------------------------------

# Risk CRUD

def createRisk(request):
    context = {}
    form = RiskForm(request.POST or None, initial={'createdBy': request.user})
    if form.is_valid():
        form.save()
        riskid = Risk.objects.last()
        return redirect('createmitigation', pk=riskid.id)

    context['form'] = form

    return render(request, 'information/risk/create.html', context)


def listRisk(request):
    context = {}
    risk = Risk.objects.filter(flag=True)
    context['risks'] = risk

    return render(request, 'information/risk/list.html', context)


def deleteRisk(request, pk):
    context = {}
    risk = Risk.objects.get(id=pk)
    riskName = risk.keyRiskIssue
    mitigation = Mitigation.objects.filter(risk_id=pk).filter(flag=True)

    if request.method == "POST":
        Risk.objects.filter(id=pk).update(flag=False)
        Mitigation.objects.filter(risk_id=pk).update(flag=False)
        return redirect('listrisk')
    context['risk'] = riskName
    context['mitigation'] = mitigation

    return render(request, 'information/risk/delete.html', context)


def updateRisk(request, pk):
    context = {}
    risk = Risk.objects.get(id=pk)
    form = RiskForm(request.POST or None, instance=risk)
    mitigation = Mitigation.objects.filter(risk_id=pk, flag=True)

    if form.is_valid():
        form.save()
        return redirect('listrisk')

    context['form'] = form
    context['mitigation'] = mitigation
    return render(request, 'information/risk/update.html', context)


def detailRisk(request, pk):
    context = {}
    risk = Risk.objects.filter(id=pk, flag=True)
    mitigation = Mitigation.objects.filter(risk_id=pk, flag=True)
    context['risk'] = risk
    context['mitigation'] = mitigation

    return render(request, 'information/risk/detail.html', context)


# --------------------------------------------------------------------------

# Mitigation CRUD

def createMitigation(request, pk):
    context = {}
    risk = Risk.objects.get(id=pk)
    form = MitigationForm(request.POST or None, initial={'risk': risk})

    if request.POST:
        if 'btn1' in request.POST and form.is_valid():
            form.save()
            return redirect('listmitigation')
        if 'btn2' in request.POST and form.is_valid():
            form.save()

    context['risk'] = risk
    context['form'] = form

    return render(request, 'information/mitigation/create.html', context)


def listMitigation(request):
    context = {}
    risk = Risk.objects.filter(flag=True)
    mitigations = Mitigation.objects.filter(flag=True)
    context['risks'] = risk
    context['mitigations'] = mitigations

    return render(request, 'information/mitigation/list.html', context)


def deleteMitigation(request, pk):
    context = {}
    mitigation = Mitigation.objects.get(id=pk)

    if request.method == "POST":
        Mitigation.objects.filter(id=pk).update(flag=False)
        return redirect('listmitigation')

    context['mitigation'] = mitigation

    return render(request, 'information/mitigation/delete.html', context)


def updateMitigation(request, pk):
    context = {}
    mitigation = Mitigation.objects.get(id=pk)
    form = MitigationForm(request.POST or None, instance=mitigation)


    if form.is_valid():
        form.save()
        return redirect('listmitigation')

    context['form'] = form
    context['mitigation'] = mitigation
    return render(request, 'information/mitigation/update.html', context)


def detailMitigation(request, pk):
    context = {}
    mitigation = Mitigation.objects.filter(id=pk, flag=True)
    context['mitigation'] = mitigation

    return render(request, 'information/mitigation/detail.html', context)
