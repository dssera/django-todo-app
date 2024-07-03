from django.http import HttpResponse

def say_hello_view(request):
    return HttpResponse("hihihi")