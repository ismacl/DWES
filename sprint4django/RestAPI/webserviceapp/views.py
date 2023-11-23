from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Tjuegos

def pagina_de_prueba(request):
	return HttpResponse("<h1>Chimichanga</h1>");

def devolver_juegos(request):
	lista = Tjuegos.objects.all()
	respuesta_final = []
	for fila_sql in lista:
		diccionario = {}
		diccionario['nombre'] = fila_sql.nombre
		diccionario['duracion_h'] = fila_sql.duracion_h
		diccionario['desarolladora'] = fila_sql.desarolladora
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)

# Create your views here.
