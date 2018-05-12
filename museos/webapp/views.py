from django.shortcuts import render
from django.http import HttpResponse
from .xmlparser import getrss
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import Museo
from .models import Comentario
from .models import Usuario
from .models import Seleccion

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

FORMULARIO_COMENTARIOS = '''
            <form action="" Method="POST">
            Introduce:<br>
            <input type="text" name="comentario" placeholder="Escriba aqui su comentario...">
            <input type="submit" value="Comentar">
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
        view_museos += '<ul><li><a href="' + museo.enlace + '">'+ museo.nombre + '</a></li><li>' + museo.direccion + '</li><li><a href="http://localhost:8000/museos/'+str(museo.id) + '">mas info</a></li></ul>'
    return HttpResponse(view_museos+'<br>'+view_usuarios+'<br>'+view_login+'<br>'+view_logout+'<br>'+boton)

def usuario(request,usuario_id):
    pagina = request.GET.urlencode().split('=')[0]
    if pagina == "":
        pagina = 0
    else:
        pagina = int(pagina) 
    selecciones = Seleccion.objects.filter(usuario_id=usuario_id)
    selecciones = selecciones[5*int(pagina):5*int(pagina+1)]
    view_museos = ""
    for seleccion in selecciones:
        view_museos += '<ul><li><a href="' + seleccion.museo.enlace + '">'+ seleccion.museo.nombre + '</a></li><li>' + seleccion.museo.direccion +'</li><li>'+ str(seleccion.fecha) +'</li><li><a href="http://localhost:8000/museos/'+str(seleccion.museo.id) + '">mas info</a></li></ul>'
    return HttpResponse(view_museos+'<br>'+str(pagina))

@csrf_exempt
def museo(request,museo_id):
    #si estas registrado pongo este formulario
    #if request.user.is_authenticated():
    #    logged = 'Logged in as ' + request.user.username
    #    log = "Logout"
    #    url = "/logout"
    #else:
    #    logged = 'Not logged in'
    #    log = "Login"
    #    url = "/login"
    museo = Museo.objects.get(id=museo_id)
    if request.method == "POST":
        aux_usuario = User.objects.get(username=request.user.username)
        aux_usuario = Usuario.objects.get(nombre_id=aux_usuario)
        aux_comentario = request.POST['comentario']
        nuevo = Comentario(usuario=aux_usuario,comentario=aux_comentario,museo=museos)
        nuevo.save()
    comentarios = Comentario.objects.filter(museo = museo)
    view_usuarios=""
    view_login = '<a href="htpp://localhost:8000/login">Iniciar sesion</a>'
    view_logout = '<a href="htpp://localhost:8000/logout">Cerrar sesion</a>'
    view_museos = "Nombre: " + museo.nombre+"<br>"+"Direccion: "+museo.direccion+"<br>"+"Enlace: "+museo.enlace + "<br>" + "Descripcion: " + museo.descripcion + "<br>" + "Barrio: "+museo.barrio+"<br>"+"Distrito: "+museo.distrito+"<br>"+"Accesibilidad: "+museo.accesibilidad+"<br>"+"Telefono: "+museo.telefono+"<br>"+"Fax: "+museo.fax+"<br>"+"Email: "+museo.email+"<br>"
    view_museos += '<h3>Lista de comentarios</h3>'
    for comentario in comentarios:
        view_museos += '<h4>'+comentario.usuario.nombre.username+'</h4>: '+comentario.comentario+'<br>'+str(comentario.fecha)
    return HttpResponse(view_museos+'<br>'+view_login+'<br>'+view_logout+"<br>"+FORMULARIO_COMENTARIOS)

@csrf_exempt
def museos(request):
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
