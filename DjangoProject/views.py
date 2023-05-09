from django.http import HttpResponse

def saludo(request):
    return  HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Chau mi amirijillo")

def edades(request, edad):
    if edad >=18:
        return HttpResponse("Usted es mayor de edad")
    else:
        return HttpResponse("Usyted es menor de edad")