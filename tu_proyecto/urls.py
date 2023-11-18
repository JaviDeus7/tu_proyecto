"""
URL configuration for tu_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('Principal/', views.pagina_principal, name='pagina_principal'),
    path('Preboda/', views.preboda, name='preboda'),
    path('Ceremonia&Celebracion/', views.ceremonia_celebracion, name='ceremonia_celebracion'),
    path('Hashtag/', views.hashtag, name='hashtag'),
    path('Musica/', views.musica, name='musica'),
    path('AlbumFotos/', views.albumFotos, name='albumFotos'),
    path('ListaBoda/', views.listaBoda, name='listaBoda'),
    path('ConfirmaAsistencia/', views.confirmaAsistencia, name='confirmaAsistencia'),
]
