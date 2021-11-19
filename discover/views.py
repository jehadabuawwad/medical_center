from .models import Malady
from django.shortcuts import render

def discover_create_view(request):
    print(request.POST)
    collected_name=request.POST.get("name")
    collected_email=request.POST.get("email")
    collected_mobile=request.POST.get("mobile")
    collected_age=request.POST.get("age")
    collected_bmi=request.POST.get("bmi")
    collected_avg_glucose_level=request.POST.get("avg_glucose_level")
    collected_ever_married=request.POST.get("ever_married")
    collected_hypertension=request.POST.get("hypertension")
    collected_work=request.POST.get("work")

    Malady.objects.create(name=collected_name,email=collected_email,mobile=collected_mobile,age=collected_age,bmi=collected_bmi,
    avg_glucose_level=collected_avg_glucose_level,ever_married=collected_ever_married,
    hypertension=collected_hypertension,work=collected_work)
    
    context={}

    return render(request,"pages/discover.html",context)
