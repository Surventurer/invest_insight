from django.shortcuts import render

def home(request):
    return render(request, 'finance_app/home.html')

def sip_calculator(request):
    sip_result = None
    if request.method == "POST" and "sip_submit" in request.POST:
        try:
            # Input values
            monthly_investment = float(request.POST.get("monthly_investment", 0))
            annual_rate = float(request.POST.get("annual_rate", 0)) / 100
            years = int(request.POST.get("years", 0))

            # Validate input
            if annual_rate <= 0 or years <= 0:
                raise ValueError("Rate of return and duration must be greater than zero.")

            n = 12
            t = years
            r = annual_rate / n

            # SIP Formula
            sip_result = monthly_investment * ((1 + r) ** (n * t) - 1) / r * (1 + r)
            sip_result = round(sip_result, 2)

        except ZeroDivisionError:
            sip_result = "Error: Division by zero occurred. Please check the input values."
        except ValueError as ve:
            sip_result = f"Error: {str(ve)}"
        except Exception as e:
            sip_result = f"Unexpected error: {str(e)}"

    return render(request, "finance_app/sip_calculator.html", {"sip_result": sip_result})

def fd_and_rd(request):
    sip_result = None
    rd_result = None
    fd_result = None

    if request.method == 'POST':
        if 'sip_submit' in request.POST:
            # SIP Calculator
            monthly_investment = float(request.POST.get('monthly_investment', 0))
            annual_rate = float(request.POST.get('annual_rate', 0))
            years = int(request.POST.get('years', 0))
            months = years * 12
            rate = annual_rate / 100 / 12
            sip_result = monthly_investment * ((1 + rate) ** months - 1) / rate * (1 + rate)

        elif 'rd_submit' in request.POST:
            # RD Calculator
            monthly_investment = float(request.POST.get('monthly_investment', 0))
            annual_interest_rate = float(request.POST.get('annual_interest_rate', 0))
            tenure = int(request.POST.get('tenure', 0))
            months = tenure * 12
            monthly_rate = annual_interest_rate / 100 / 12
            rd_result = monthly_investment * ((1 + monthly_rate) ** months - 1) / monthly_rate * (1 + monthly_rate)

        elif 'fd_submit' in request.POST:
            # FD Calculator
            principal_amount = float(request.POST.get('principal_amount', 0))
            annual_interest_rate = float(request.POST.get('annual_interest_rate', 0))
            tenure = int(request.POST.get('tenure', 0))
            fd_result = principal_amount * (1 + annual_interest_rate / 100) ** tenure

    return render(request, 'finance_app/fd_and_rd.html', {
        'sip_result': round(sip_result, 2) if sip_result else None,
        'rd_result': round(rd_result, 2) if rd_result else None,
        'fd_result': round(fd_result, 2) if fd_result else None,
    })

def real_estate(request):
    return render(request, 'finance_app/real_estate.html')

def commodities(request):
    return render(request, 'finance_app/commodities.html')

# RD Calculator
def rd_calculator(request):
    if request.method == 'POST':
        monthly_investment = float(request.POST.get('monthly_investment', 0))
        annual_interest_rate = float(request.POST.get('annual_interest_rate', 0))
        years = int(request.POST.get('years', 0))
        
        months = years * 12
        monthly_rate = annual_interest_rate / 100 / 12
        maturity_value = monthly_investment * ((1 + monthly_rate) ** months - 1) * (1 + monthly_rate) / monthly_rate
        
        return render(request, 'finance_app/rd_calculator.html', {
            'maturity_value': round(maturity_value, 2),
        })
    return render(request, 'finance_app/rd_calculator.html')

def rd_page(request):
    maturity_value = None
    if request.method == 'POST':
        monthly_investment = float(request.POST.get('monthly_investment', 0))
        annual_interest_rate = float(request.POST.get('annual_interest_rate', 0))
        tenure = int(request.POST.get('tenure', 0))

        months = tenure * 12
        monthly_rate = annual_interest_rate / 100 / 12
        maturity_value = monthly_investment * ((1 + monthly_rate) ** months - 1) / monthly_rate * (1 + monthly_rate)

    return render(request, 'finance_app/rd_page.html', {
        'maturity_value': round(maturity_value, 2) if maturity_value else None,
    })


def fd_page(request):
    maturity_value = None
    if request.method == 'POST':
        principal_amount = float(request.POST.get('principal_amount', 0))
        annual_interest_rate = float(request.POST.get('annual_interest_rate', 0))
        tenure = int(request.POST.get('tenure', 0))

        maturity_value = principal_amount * (1 + annual_interest_rate / 100) ** tenure

    return render(request, 'finance_app/fd_page.html', {
        'maturity_value': round(maturity_value, 2) if maturity_value else None,
    })


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calculate_rd(request):
    if request.method == "POST":
        try:
            monthly_investment = float(request.POST.get("monthly_investment"))
            annual_interest_rate = float(request.POST.get("annual_interest_rate")) / 100
            tenure = int(request.POST.get("tenure"))

            # RD Maturity Formula
            n = tenure * 12
            i = annual_interest_rate / 12
            maturity_value = monthly_investment * ((1 + i) ** n - 1) / i

            return JsonResponse({"rd_result": round(maturity_value, 2)})
        except Exception as e:
            return JsonResponse({"error": str(e)})

@csrf_exempt
def calculate_fd(request):
    if request.method == "POST":
        try:
            principal_amount = float(request.POST.get("principal_amount"))
            annual_interest_rate = float(request.POST.get("annual_interest_rate")) / 100
            tenure = int(request.POST.get("tenure"))

            # FD Maturity Formula
            maturity_value = principal_amount * ((1 + annual_interest_rate) ** tenure)

            return JsonResponse({"fd_result": round(maturity_value, 2)})
        except Exception as e:
            return JsonResponse({"error": str(e)})
