from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def bmi_form(request):
    result = None
    category = ''
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height']) / 100  # Convert cm to meters
        bmi = round(weight / (height ** 2), 2)

        # Categorize BMI
        if bmi < 18.5:
            category = 'Underweight'
        elif bmi >= 18.5 and bmi < 24.9:
            category = 'Normal'
        elif bmi >=25 and bmi < 29.9:
            category = 'Overweight'
        else:
            category = 'Obese'

        result = {'bmi': bmi, 'category': category}

    return render(request, 'bmi.html', {'result': result})