from django.shortcuts import render

# Create your views here.



def viewList(request):
    return render(request,'indicators/indicatorsList.html')


def detailVew(request):
    return render(request,'indicators/indicator_detail.html')