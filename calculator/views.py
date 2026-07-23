from django.shortcuts import render
from django.http import JsonResponse
from .logic import calcolatore_liquido
# Create your views here.

def calcolatore_view(request):

    ml_richiesti = request.GET.get('ml_richiesti', 0)
    nico_target = request.GET.get('nico_target', 0)
    percentuale_aroma = request.GET.get('percentuale_aroma', 0)

    risultato_calcolo = calcolatore_liquido(float(nico_target), float(ml_richiesti), float(percentuale_aroma))
    return JsonResponse(risultato_calcolo)

def index(request):
    return render(request, 'calculator/index.html')

