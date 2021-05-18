from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms


# Set Validator for rating
def validate_number5(value):
    if value > 5 or value < 1:
        raise forms.ValidationError(
            _('%(value) is not between 1 to 5'),
            params={'value': value},
        )


def validate_number25(value):
    if value > 25 or value < 1:
        raise forms.ValidationError(
            _('%(value) is not between 1 to 25'),
            params={'value': value},
        )


# Corprate Objective model

class CorprateObjective(models.Model):
    name = models.CharField(max_length=300)
    log = HistoricalRecords()
    flag = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Division Model

class Division(models.Model):
    division = models.CharField(max_length=350)
    log = HistoricalRecords
    flag = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.division


# Owner model that will change to active directory

class Owners(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    log = HistoricalRecords
    flag = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# BIZ KPIs Model

class BizKPI(models.Model):
    kpi = models.TextField()
    log = HistoricalRecords()
    flag = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kpi


# Principal Risk model

class PrincipalRisk(models.Model):
    prNumber = models.IntegerField()
    prShortTitile = models.CharField(max_length=350)
    prCompleteTiyle = models.TextField()
    riskCategory = models.CharField(max_length=350)
    owner = models.ManyToManyField(Owners, blank=True)
    riskPreference = models.TextField()
    inherent = models.IntegerField(default=1, validators=[validate_number25])
    residual = models.IntegerField(default=1, validators=[validate_number25])
    target = models.IntegerField(default=1, validators=[validate_number25])
    log = HistoricalRecords()
    flag = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prShortTitile


# velocity

velocity = [
    ('1', 'Low'),
    ('2', 'Medium'),
    ('3', 'High')
]


# Risk Model

class Risk(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    corprateObjective = models.ManyToManyField(CorprateObjective, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    bizKPI = models.ManyToManyField(BizKPI, blank=True)
    principakRisk = models.ForeignKey(PrincipalRisk, on_delete=models.SET_NULL, null=True, blank=True)
    keyRiskIssue = models.CharField(max_length=400)
    description = models.TextField()
    cause = models.TextField()
    effect = models.TextField()
    inherentprob = models.IntegerField(default=1, validators=[validate_number5])
    inherentimpact = models.IntegerField(default=1, validators=[validate_number5])
    inherentrate = models.IntegerField(default=1, validators=[validate_number25])
    residiualprob = models.IntegerField(default=1, validators=[validate_number5])
    residiualimpact = models.IntegerField(default=1, validators=[validate_number5])
    residiualrate = models.IntegerField(default=1, validators=[validate_number25])
    targetProb = models.IntegerField(default=1, validators=[validate_number5])
    targetImpact = models.IntegerField(default=1, validators=[validate_number5])
    targetRate = models.IntegerField(default=1, validators=[validate_number25])
    contorlInplace = models.TextField()
    riskVelocity = models.CharField(choices=velocity, max_length=10, default='1')
    log = HistoricalRecords()
    flag = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyRiskIssue


# Status
status = [
    ('1', 'Open'),
    ('2', 'Closed'),
    ('3', 'Overdue'),
    ('4', 'Cancelled'),
    ('5', 'Not Overdue'),
]


# Mitigation model

class Mitigation(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    mitigation = models.TextField()
    status = models.CharField(choices=status,
                              default='1', max_length=10)
    owner = models.ManyToManyField(Owners, blank=True)
    dueDate = models.DateTimeField(null=True, blank=True)
    initialDueDate = models.DateTimeField()
    log = HistoricalRecords()
    flag = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mitigation
