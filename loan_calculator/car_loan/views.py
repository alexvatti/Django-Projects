from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def calculate_emi(principal, rate, tenure):
    r = rate / (12 * 100)
    n = tenure * 12
    emi = principal * r * ((1 + r) ** n) / ((1 + r) ** n - 1)
    total_payment = round(emi * n, 2)
    total_interest = round(total_payment - principal, 2)
    return round(emi), total_interest, total_payment

def car_loan_view(request):
    result = None
    if request.method == 'POST':
        p = float(request.POST.get('principal', 1000000))  # Default ₹10L
        r = float(request.POST.get('rate', 9.0))           # Default 9% rate
        t = int(request.POST.get('tenure', 5))             # Default 5 years
        emi, interest, total = calculate_emi(p, r, t)
        result = {
            'emi': emi,
            'total_interest': interest,
            'total_payment': total
        }
    return render(request, 'car_loan.html', {'result': result})

