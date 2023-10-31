from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, Http404
def index(request):
    return HttpResponse("Страница сайта")

def categories(request, peopleid):
    if int(peopleid) > 200:
        raise Http404()
    return HttpResponse(f"<h1>Что-то про пользователя</h1><p>{peopleid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
