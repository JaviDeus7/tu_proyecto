from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    return render(request, 'boda/bienvenida.html')

def pagina_principal(request):
    return render(request, 'boda/pagina_principal.html')