from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from .models import Problem

def say_hello_view(request):
    return HttpResponse("hihihi")


def index_view(request: HttpRequest):
    print(request.POST.get('id', None))
    if request.method == "GET":
        problems = Problem.objects.all()
        return render(request, 'todo/index.html', {'problems': problems})
    elif request.method == "POST":
        problems = Problem.objects.all()
        problem_on_update = Problem.objects.get(id=request.POST.get('id', None))
        problem_on_update.reverse_and_save()
        return render(request, 'todo/index.html', {'problems': problems})

def create_problem(request: HttpRequest):
    if request.method == 'POST':
        problem = Problem()
        problem.title = request.POST.get('title')
        problem.save()
    return HttpResponseRedirect('/')

def delete_problem(request: HttpRequest):
    if request.method == 'POST':
        try:
            problem = Problem.objects.get(id=request.POST.get('id'))
            problem.delete()
        except Problem.DoesNotExist:
            return HttpResponseNotFound('<h2>Problem doesn\'t found.</h2>')
    return HttpResponseRedirect('/')
    