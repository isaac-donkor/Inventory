from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import InvoiceItem
from django.contrib import admin
from django import forms
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
import json

def smenns(request):
    template=loader.get_template('gold_calculator.html')
    return HttpResponse(template.render())

def gold_calculator(request):
    if request.method == 'POST':
        weight_grams = float(request.POST.get('weight-grams'))
        price_gold = float(request.POST.get('price-gold'))
        volume = float(request.POST.get('volume'))
        weight_pounds = weight_grams / 7.75
        density = weight_pounds / volume
        karat = (density - 10.51) * 52.838 / density
        amount_gold = (karat / 23) * price_gold * weight_pounds

        if request.POST.get('action') == 'add_item':
            current_calculation = {
            'item': f'Item {InvoiceItem.objects.count() + 1}',
            'weight_pounds': round(weight_pounds, 2),
            'karat': round(karat, 2),
            'amount_gold': round(amount_gold, 2),
        }
            return JsonResponse(current_calculation)
        else:
            InvoiceItem.objects.create(
                item_name=current_calculation['item'],
                weight_pounds=current_calculation['weight_pounds'],
                karat=current_calculation['karat'],
                amount_gold=current_calculation['amount_gold']
            )

    if request.method == "GET":
            
            return render(request, 'gold_calculator.html', 
                        #   {'current_calculation': current_calculation}
                          )

def sales_view(request):
     template=loader.get_template('sales_view.html')
     objects=InvoiceItem.objects.all()
     return render(request,'sales_view.html',{'objects':objects})

def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = EmailMessage(
            subject='Invoice',
            body=f'Here is your invoice:\n\n{data["content"]}',
            to=['justinkwakye50@gmail.com']
        )
        email.send()
        return JsonResponse({'status': 'success'})