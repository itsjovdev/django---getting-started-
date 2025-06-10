# importamos la funcion path, que se usa para definir rutas URL
from django.urls import path
from . import views
urlpatterns = [
    path("<int:day>", views.days_week_with_number),
    # El parámetro 'name' es un alias o identificador único para esta ruta.
    path("<str:day>", views.days_week, name="day-quote") #/quotes/friday
]