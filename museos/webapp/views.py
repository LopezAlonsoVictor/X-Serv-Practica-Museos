from django.shortcuts import render
from django.http import HttpResponse
from .xmlparser import getrss
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Museo
from .models import Comentario
from .models import Usuario

# Create your views here.

FILT_ACCESIBILIDAD_POST = '''
            <form action="" Method="POST">
            <input type="submit" value="Accesibles">
</form>
'''

FILT_ACCESIBILIDAD_GET = '''
            <form action="" Method="GET">
            <input type="submit" value="Todos">
</form>
'''

def contador(comentarios):
    lista = {}
    for comentario in comentarios:
        if comentario.museo.nombre in lista:
            lista[comentario.museo.nombre] = lista[comentario.museo.nombre] + 1
        else:
            lista[comentario.museo.nombre] = 1
    return lista

def mascomentarios(lista,museos_mostrar):
    museos = []
    iteraciones = museos_mostrar
    if len(lista) < museos_mostrar:
        iteraciones = len(lista)
    for i in range(0,iteraciones):
        aux = 0
        museo = ""
        for elemento in lista:
            if lista[elemento] >= aux:
                aux = lista[elemento]
                museo = elemento
        lista[museo] = 0
        museos.append(museo)
    return museos

def filtaccesibilidad(lista):
    aux = []
    for i in range(0,len(lista)):
        museo = Museo.objects.get(nombre=lista[i])
        if int(museo.accesibilidad) == 1:
            aux.append(lista[1])
    return aux

def getbarrios(museos):
    aux = []
    for museo in museos:
       aux.append(museo.barrio)
    aux = list(set(aux))
    return aux

def menu_filtrado(barrios):
    aux = '''<form action="" Method="POST" id="respuesta">
            <input type="submit" value="Enviar">
            </form>
            <select name="barrio" form="respuesta">
    '''
    for barrio in barrios:
        aux += '<option value="'+barrio+'">'+barrio+'</option>'
    aux += '</select>'
    return aux

@csrf_exempt
def barra(request):
    museos_mostrar = 5
    boton = FILT_ACCESIBILIDAD_POST
    view_museos = ""
    view_usuarios = "<ul>"
    view_login = '<a href="htpp://localhost:8000/login">Iniciar sesion</a>'
    view_logout = '<a href="htpp://localhost:8000/logout">Cerrar sesion</a>'
    comentarios = Comentario.objects.all()
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        view_usuarios += '<li><a href="http://localhost:8000/usuario/'+str(usuario.id)+'">'+usuario.nombre.username+'</a></li>'
    view_usuarios += '</ul>'
    lista = contador(comentarios)
    lista = mascomentarios(lista,museos_mostrar)
    if request.method == "POST":
        lista = filtaccesibilidad(lista)
        boton = FILT_ACCESIBILIDAD_GET
    for i in range(0,len(lista)):
        museo = Museo.objects.get(nombre=lista[i])
        view_museos += '<ul><li><a href="' + museo.enlace + '">'+ museo.nombre + '</a></li><li>' + museo.direccion + '</li><li><a href="http://localhost:8000/museo/' + str(museo.id) + '">mas info</a></li></ul>'
    return HttpResponse(view_museos+'<br>'+view_usuarios+'<br>'+view_login+'<br>'+view_logout+'<br>'+boton)

def usuario(request):
    return HttpResponse("holaaaa")

@csrf_exempt
def museos(request):
    print(request)
    museos = Museo.objects.all()
    barrios = getbarrios(museos)
    menu = menu_filtrado(barrios)
    view_museos = '<ul>'
    if request.method == "POST":
        museos = Museo.objects.filter(barrio=request.POST['barrio'])
    for museo in museos:
        view_museos += '<li><a href="http://localhost:8000/museos/'+str(museo.id)+'">'+museo.nombre+'</a></li>'
    view_museos += '</ul>'
    return HttpResponse(menu+'<br>'+view_museos)

def update(request):
    Museo.objects.all().delete()
    getrss()
    return redirect("http://localhost:8000")
