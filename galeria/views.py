from django.shortcuts import render

dados = {
    1:{"nome": "Nebulosa de Carina",
       "legenda": "webbtelescope.org / NASA / James Webb"},
    2:{"nome": "Gláxia NGC 1079",
       "legenda": "nasa.org / NASA / Hubble"},
}

def index(request):
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')