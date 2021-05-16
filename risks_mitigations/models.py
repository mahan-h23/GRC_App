from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django import forms


def validate_number(value):
    if value >5 or value < 1:
        raise forms.ValidationError(
            _('%(value) is not between 1 to 5'),
            params={'value':value},
        )

divisions = [
    ('TECH','Tech'),
    ('OPERATION','Operation'),
    ('COMMERCIAL','Commercial'),
    ('LEGAL','Legal'),
    ('MARKETING','Marketing'),
    ('FIANCE','Finance'),
    ('CX','CX'),
    ('BD','BD'),
    ('HR','HR')
]


class Risk(models.Model):

    division = models.CharField(max_length=100 , choices=divisions ,default='TECH')
    riskname = models.CharField(max_length=300)
    riskdiscription = models.TextField
    risknameCause = models.CharField(max_length=500)
    riksEffect = models.CharField(max_length=500)
    inherent = models.IntegerField(default=1,
        validators=[validate_number])

    recidual = models.IntegerField(default=1,
                                   validators=[validate_number])
    target = models.IntegerField(default=1,
        validators=[validate_number])
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User,on_delete=models.SET_NULL,null=True ,related_name='riskcreate')

    def __str__(self):
        return self.riskname




class Mitigation(models.Model):

    risk = models.ForeignKey(Risk,on_delete=models.CASCADE , related_name='risks')
    mitigation = models.CharField(max_length=500)
    owner = models.CharField(max_length=250)
    dueDate = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.mitigation

