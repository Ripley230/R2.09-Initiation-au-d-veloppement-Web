from django.shortcuts import render

def index(request):
    return render(request, 'myfirstapp/index.html')

def bonjour(request):
    nom=request.GET["nom"]
    return render(request,'myfirstapp/bonjour.html',{"nom":nom})