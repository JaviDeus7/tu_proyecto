from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    return render(request, 'boda/bienvenida.html')

def pagina_principal(request):
    return render(request, 'boda/pagina_principal.html')

def ceremonia(request):
    return render(request, 'boda/ceremonia.html')

def celebracion(request):
    return render(request, 'boda/celebracion.html')

def hashtag(request):
    return render(request, 'boda/hashtag.html')

def musica(request):
    return render(request, 'boda/musica.html')

def albumFotos(request):
    return render(request, 'boda/albumfotos.html')

def listaBoda(request):
    return render(request, 'boda/listaBoda.html')

def confirmaAsistencia(request):
    return render(request, 'boda/confirmaAsistencia.html')
