from django.http import HttpResponse
def index(request):
    return HttpResponse("hello");

def About(request):
    return HttpResponse("hello Monjur");