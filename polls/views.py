from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import  *

from django.template import loader, RequestContext
# Create your views here.
def index(request):
    latest_question = Question.objects.order_by('pub_date')[:5]
    context = {'latest_questions': latest_question}
    return render (request, 'polls/index.html',context)

def detail(response,question_id):
    return HttpResponse('detail view of the question: %s' %question_id)

def results(response ,question_id):
    return HttpResponse("results of the question : %s" %question_id)
def vote( response,question_id):
    return HttpResponse("vote on question: %s" %question_id)
def envia(request,lat,long):
    coord = Coordenadas(latitude = lat, longitude = long)
    coord.save()
    dicionario = {'latitude':lat,'longitude':long}
    return HttpResponse()
def get(request):
    coord = Coordenadas.objects.latest('id')
    return JsonResponse({'lat':coord.latitude,'long':coord.longitude})