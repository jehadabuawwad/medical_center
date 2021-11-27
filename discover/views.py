from .models import Malady
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def discover_create_view(request):
    collected_name = request.POST.get("name")
    collected_email = request.POST.get("email")
    collected_mobile = request.POST.get("mobile")

    collected_age = request.POST.get("age")
    collected_bmi = request.POST.get("bmi")
    collected_avg_glucose_level = request.POST.get("avg_glucose_level")

    collected_gender = request.POST.get("gender")
    collected_residence_type = request.POST.get("residence_type")
    collected_ever_married = request.POST.get("ever_married")
    collected_work_type = request.POST.get("work_type")
    collected_smoking_status = request.POST.get("smoking_status")
    collected_hypertension = request.POST.get("hypertension")
    collected_heart_disease = request.POST.get("heart_disease")

    collection = []
    collection += [
        collected_age,
        collected_bmi,
        collected_avg_glucose_level,
        collected_gender,
        collected_ever_married,
        collected_residence_type,
        collected_heart_disease,
        collected_hypertension,
    ]
    collected_smoking_status = collected_smoking_status.split(",")
    collected_work_type = collected_work_type.split(",")
    modified_colloection = []
    for item in collected_smoking_status:
        collection += [item]
    for item in collected_work_type:
        collection += [item]
    for item in collection:
        modified_colloection.append(float(item))
    from .predictor import AIModel

    instance = AIModel()
    predicted_status = instance.predict(modified_colloection)

    if predicted_status == 0:
        predicted_status = "Negative"
    elif predicted_status == 1:
        predicted_status = "Positve"
    else:
        predicted_status = "Unkown"
    Malady.objects.create(
        name=collected_name,
        email=collected_email,
        mobile=collected_mobile,
        age=collected_age,
        bmi=collected_bmi,
        avg_glucose_level=collected_avg_glucose_level,
        gender=collected_gender,
        residence_type=collected_residence_type,
        ever_married=collected_ever_married,
        work_type=collected_work_type,
        smoking_status=collected_smoking_status,
        hypertension=collected_hypertension,
        heart_disease=collected_heart_disease,
        status=predicted_status,
    )

    context = {}

    return render(request, "pages/discover.html", context)


class ResultListView(ListView):
    template_name = "pages/result_list.html"
    model = Malady
    context_object_name = "result_list"


class ResultDetailView(DetailView):
    template_name = "pages/result_detail.html"
    model = Malady
