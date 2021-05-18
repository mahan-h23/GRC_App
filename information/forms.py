from .models import *
from django.forms import ModelForm, SelectDateWidget
from django.utils.translation import ugettext_lazy as _


class CorprateForm(ModelForm):
    class Meta:
        model = CorprateObjective
        fields = '__all__'
        labels = {
            'name': _('Corporate Objective:'),
            'flag': _('Not Hidden:')
        }


class DivisionForm(ModelForm):
    class Meta:
        model = Division
        fields = '__all__'
        labels = {
            'division': _('Division:'),
            'flag': _('Not Hidden:')
        }


class OwnerForm(ModelForm):
    class Meta:
        model = Owners
        fields = '__all__'
        labels = {
            'first_name': _('First Name:'),
            'last_name': _('Last Name:'),
            'division': _('Select Division:'),
            'flag': _('Not Hidden:')

        }


class BizKpiForm(ModelForm):
    class Meta:
        model = BizKPI
        fields = '__all__'
        labels = {
            'kpi': _('Biz KPI:'),
            'flag': _('Not Hidden:')

        }


class PrincipalForm(ModelForm):
    class Meta:
        model = PrincipalRisk
        fields = '__all__'
        labels = {
            'prNumber': _('Principal Number:'),
            'prShortTitile': _('Principal Short Title:'),
            'prCompleteTiyle': _('Principal Complete Title:'),
            'riskCategory': _('Risk Category:'),
            'owner': _('Owner:'),
            'riskPreference': _('Risk Preferences:'),
            'inherent': _('Principal Inherent Rating:'),
            'residual': _('Principal Residual Rating:'),
            'target': _('Principal Target Rating'),
            'flag': _('Not Hidden:')

        }


class RiskForm(ModelForm):
    class Meta:
        model = Risk
        fields = '__all__'
        labels = {
            'createdBy': _('Added By:'),
            'corprateObjective': _('Corporate Objectives:'),
            'division': _('Division:'),
            'bizKPI': _('Biz KPIs:'),
            'principakRisk': _('Principal Risk:'),
            'keyRiskIssue': _('Key Risk Issue:'),
            'description': _('Risk Description:'),
            'cause': _('Risk Causes:'),
            'effect': _('Risk Effects'),
            'inherentprob': _('Inherent Probability:'),
            'inherentimpact': _('Inherent Impact:'),
            'inherentrate': _('Inherent Rate:'),
            'residiualprob': _('Residual Probability:'),
            'residiualimpact': _('Residual Impact:'),
            'residiualrate': _('Residual Rate:'),
            'targetProb': _('Target Probability:'),
            'targetImpact': _('Target Impact:'),
            'targetRate': _('Target Rate:'),
            'contorlInplace': _('Controls inplace:'),
            'riskVelocity': _('Risk Velocity:'),
            'flag': _('Not Hidden:')

        }

    def __init__(self, *args, **kwargs):
        super(RiskForm, self).__init__(*args, **kwargs)
        self.fields['createdBy'].disabled = True


class MitigationForm(ModelForm):
    class Meta:
        model = Mitigation
        fields = '__all__'
        labels = {
            'risk': _('Related Risk:'),
            'mitigation': _('Mitigation:'),
            'status': _('Status:'),
            'owner': _('Risk Owner:'),
            'dueDate': _('Due Date:'),
            'initialDueDate': _('Initial Due Date:'),
            'flag': _('Not Hidden:')
        }
