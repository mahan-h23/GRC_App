from django.shortcuts import render
from information.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


# For the first chart in dashborard Risk based on divsion and SPIDER chart
class ChartBasedDivision(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        veryhigh = []
        high = []
        medium = []
        low = []
        total = []
        # set Query for division and used for filter
        division = list(Division.objects.values_list('division', flat=True))

        for x in division:
            vh = Risk.objects.filter(Q(division__division=x) & Q(residiualrate__gte=25)).count()
            veryhigh.append(vh)
            h = Risk.objects.filter(
                Q(division__division=x) & Q(residiualrate__gte=15) & Q(residiualrate__lte=20)).count()
            high.append(h)
            m = Risk.objects.filter(
                Q(division__division=x) & Q(residiualrate__gte=6) & Q(residiualrate__lte=14)).count()
            medium.append(m)
            l = Risk.objects.filter(
                Q(division__division=x) & Q(residiualrate__gte=1) & Q(residiualrate__lte=5)).count()
            low.append(l)
            t = Risk.objects.filter(division__division=x).count()
            total.append(t)

        data = {
            "division": division,
            "veryhigh": veryhigh,
            "medium": medium,
            "low": low,
            "total": total
        }
        return Response(data)


# Total Risk piechart in dashboard

class TotalRisk(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        total = []
        veryhigh = Risk.objects.filter(Q(residiualrate__gte=25)).count()
        total.append(veryhigh)
        high = Risk.objects.filter(Q(residiualrate__gte=15) & Q(residiualrate__lte=20)).count()
        total.append(high)
        medium = Risk.objects.filter(Q(residiualrate__gte=6) & Q(residiualrate__lte=14)).count()
        total.append(medium)
        low = Risk.objects.filter(Q(residiualrate__gte=1) & Q(residiualrate__lte=5)).count()
        total.append(low)

        data = {
            "data": total
        }

        return Response(data)


# Mitigation Summary chart in dashboard per division

class MitigationSummary(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        overdue = []
        open = []
        closed = []
        total = []
        # set Query for division and used for filter
        division = list(Division.objects.values_list('division', flat=True))

        for x in division:
            vh = Risk.objects.filter(
                Q(division__division=x) & Q(mitigation__status=3) & Q(mitigation__flag=True)).values_list(
                'mitigation').count()
            overdue.append(vh)
            h = Risk.objects.filter(
                Q(division__division=x) & Q(mitigation__status=1) & Q(mitigation__flag=True)).values_list(
                'mitigation').count()
            open.append(h)
            m = Risk.objects.filter(
                Q(division__division=x) & Q(mitigation__status=2) & Q(mitigation__flag=True)).values_list(
                'mitigation').count()
            closed.append(m)
            l = Risk.objects.filter(
                Q(division__division=x) & Q(mitigation__flag=True)).values_list('mitigation').count()
            total.append(l)

        data = {
            "label": division,
            "overdue": overdue,
            "open": open,
            "closed": closed,
            "total": total
        }

        return Response(data)


# Total Mitigation piechart in dashboard

class TotalMitigation(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        total = []

        veryhigh = Risk.objects.filter(Q(residiualrate__gte=25) & Q(mitigation__flag=True)).values_list(
            'mitigation').count()
        total.append(veryhigh)
        high = Risk.objects.filter(
            Q(residiualrate__gte=15) & Q(residiualrate__lte=20) & Q(mitigation__flag=True)).values_list(
            'mitigation').count()
        total.append(high)
        medium = Risk.objects.filter(
            Q(residiualrate__gte=6) & Q(residiualrate__lte=14) & Q(mitigation__flag=True)).values_list(
            'mitigation').count()
        total.append(medium)
        low = Risk.objects.filter(
            Q(residiualrate__gte=1) & Q(residiualrate__lte=5) & Q(mitigation__flag=True)).values_list(
            'mitigation').count()
        total.append(low)

        data = {
            "data": total
        }

        return Response(data)


# individual bar Chart for division risk and get type

class DivisonIndividual(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, type, format=None):
        total = []

        veryhigh = Risk.objects.filter(Q(residiualrate__gte=25) & Q(division__division=type)).count()
        total.append(veryhigh)
        high = Risk.objects.filter(
            Q(residiualrate__gte=15) & Q(residiualrate__lte=20) & Q(division__division=type)).count()
        total.append(high)
        medium = Risk.objects.filter(
            Q(residiualrate__gte=6) & Q(residiualrate__lte=14) & Q(division__division=type)).count()
        total.append(medium)
        low = Risk.objects.filter(
            Q(residiualrate__gte=1) & Q(residiualrate__lte=5) & Q(division__division=type)).count()
        total.append(low)

        data = {
            "data": total
        }

        return Response(data)


# individual piechart Chart for division mitigation and get type

class MitigationperDivision(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, type, format=None):
        total = []
        veryhigh = Risk.objects.filter(
            Q(residiualrate__gte=25) & Q(division__division=type) & Q(mitigation__flag=True)).values_list(
            'mitigation').count()
        total.append(veryhigh)
        high = Risk.objects.filter(
            Q(residiualrate__gte=15) & Q(residiualrate__lte=20) & Q(division__division=type) & Q(
                mitigation__flag=True)).values_list('mitigation').count()
        total.append(high)
        medium = Risk.objects.filter(
            Q(residiualrate__gte=6) & Q(residiualrate__lte=14) & Q(division__division=type) & Q(
                mitigation__flag=True)).values_list('mitigation').count()
        total.append(medium)
        low = Risk.objects.filter(
            Q(residiualrate__gte=1) & Q(residiualrate__lte=5) & Q(division__division=type) & Q(
                mitigation__flag=True)).values_list('mitigation').count()
        total.append(low)

        data = {
            "data": total
        }

        return Response(data)
