from django.shortcuts import render
from .models import Currency
import requests


def index(request):
    if request.method == "POST":
        try:
            amount = float(request.POST.get('amount'))
            from_money = request.POST.get("currency_from")
            to_money = request.POST.get("currency_to")
        except ValueError:
            return render(request, 'index.html', {'error': 'Please enter a number'})
        url = f"https://open.er-api.com/v6/latest/{from_money}"
        res = requests.get(url).json()
        if res["result"] == "success":
            summa = res["rates"][to_money]
            result = summa * amount
            context = {
                "result": result,
                "currency_to": to_money,
            }
            return render(request, "index.html", context)
    return render(request, "index.html")
