from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
#Una vista es un accionable, hay dos maneras de hacer: por funciones y por clases.

days_of_week = {
    "monday" : "lunes",
    "tuesday" : "martes",
    "wednesday" : "miercoles",
    "thursday" : "jueves"
}


def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("No hay frase para este dia")

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El dia no existe")
    redirect_day = days[day-1]
    return HttpResponseRedirect(f"/quotes/{redirect_day}")