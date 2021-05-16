from django.forms import ModelForm,SelectDateWidget
from django.utils.translation import ugettext_lazy as _
from .models import *



class RiskForm(ModelForm):
    class Meta:
        model = Risk
        exclude = ['createdDate','updateDate']
        labels = {
            'createdBy':_('Added by'),
            'riskname':_('Key Risk Isue'),
            'risknameCause':_('Risk Cause'),
            'Risk Effect':_('Risk Effect'),
            'inherent':_('Inherent Rating'),
            'recidual':_('Residual '),

        }


    def __init__(self,*args,**kwargs):
        super(RiskForm, self).__init__(*args,**kwargs)
        self.fields['createdBy'].disabled = True



class MitigationForm(ModelForm):
    class Meta:
        model = Mitigation
        fields = '__all__'
        widgets = {
            'dueDate': SelectDateWidget
        }

    def __init__(self,*args,**kwargs):
        super(MitigationForm, self).__init__(*args,**kwargs)
        self.fields['risk'].disabled = True
        self.fields['mitigation'].widget.attrs['style'] = 'width:400px; height:40px;'
        self.fields['dueDate'].widget.attrs['style'] = 'width:80px; height:20px;'
        self.fields['risk'].widget.attrs['style'] = 'width:200px; height:40px;'





