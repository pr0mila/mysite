from django.http import HttpResponse

def index(respose):
    return HttpResponse("Hello Monty Python!")
