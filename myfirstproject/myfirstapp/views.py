from django.shortcuts import render

def index(request):
    return render(request, 'myfirstapp/index.html')

def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')

def main(request):
    return render(request, 'myfirstapp/main.html')

def bonjour(request):
    nom=request.GET["nom"]
    prenom = request.GET["prenom"]
    age = request.GET["age"]
    return render(request, 'myfirstapp/index.html', {"nom": nom, "prenom": prenom, "age": age})