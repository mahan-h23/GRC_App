from django.urls import path
from .views import *

urlpatterns = [
    path('riskbased/', ChartBasedDivision.as_view(), name='riskbaseddivision'), # For the first chart in dashborard Risk based on divsion and SPIDER chart
    path('totalrisk/',TotalRisk.as_view(), name = 'totalrisk'), # for total risk piechart in dashboard
    path('mitigationsummary/',MitigationSummary.as_view(), name = 'mitigationsummary'), # Mitigation Summary chart in dashboard per division
    path('totalmitigation/',TotalMitigation.as_view() , name = 'totalmitigation'), # Total Mitigation piechart in dashboard
    path('perdivision/<str:type>',DivisonIndividual.as_view(), name = 'perdivision'), # individual bar Chart for division risk and get type
    path('permitigation/<str:type>',MitigationperDivision.as_view(), name = 'mitigationperdivision'),# individual piechart Chart for division mitigation and get type
]
