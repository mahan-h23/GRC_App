from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

divisions = [
    ('TECH','Tech'),
    ('BD','BD'),
    ('CX','CX'),
    ('HR','HR'),
    ('OPERATION','Operation'),
    ('FINANCE','Finance'),
    ('MARKETING','Marketing'),
    ('LEGAL','Legal'),
    ('CROSSFUN','CrossFunctional')

]



#
# class Risks(models.Model):
#     division = models.CharField(max_length=250 , choices=divisions , default='TECH')
#     riskname = models.CharField(max_length=300)
#     riskdescription = models.CharField(max_length=650)
#     riskcause = models.CharField(max_length=600)
#     riskeffect = models.CharField(max_length=600)
#     inherent = models.IntegerField
#     residual = models.IntegerField
#     targetrate = models.IntegerField
#     createdby = models.ForeignKey(User , on_delete= models.SET_NULL,null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#
#     def __str__(self):
#         return self.riskname
#
#
#
#
#
#
# class Mitigations(models.Model):
#     risk = models.ForeignKey(Risks,on_delete=models.CASCADE)
#     mitigation = models.CharField(max_length=500)
#     owner = models.CharField(max_length=500)
#     duedate = models.DateTimeField(default= timezone.now)
#
#
#     def __str__(self):
#         return self.mitigation
