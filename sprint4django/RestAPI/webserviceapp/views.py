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
		diccionario['juego_id'] = fila_sql.juego_id
		diccionario['nombre'] = fila_sql.nombre
		diccionario['url_imagen'] = fila_sql.url_imagen
		diccionario['duracion_h'] = fila_sql.duracion_h
		diccionario['desarolladora'] = fila_sql.desarolladora
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)

def devolver_juegos_por_id(request, id_solicitado):
	juego = Tjuegos.objects.get(id = id_solicitado)
	comentarios = juego.tcomentarios_set.all()
	lista_comentarios = []
	for fila_comentario_sql in comentarios:
		diccionario = {}
		diccionario['juego_id'] = fila_comentario_sql.juego_id
		diccionario['comentario'] = fila_comentario_sql.comentario
		lista_comentarios.append(diccionario)
	resultado = {
		'juego_id': juego.id,
		'titulo': juego.nombre,
		'url_imagen':juego.url_imagen,
		'duracion_h':juego.duracion_h,
		'desarolladora':juego.desarolladora,
		'comentarios':lista_comentarios
	}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascil': False})

# Create your views here.
