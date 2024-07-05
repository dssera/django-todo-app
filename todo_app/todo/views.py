from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from django.shortcuts import redirect, render

from .models import Problem

def say_hello_view(request):
    return HttpResponse("hihihi")


def index_view(request: HttpRequest):
    if request.method == "GET":
        problems = Problem.objects.all()
        template = loader.get_template('todo/index.html')
        return HttpResponse(template.render({'problems': problems}, request))
        # these 2 strings can be replace on render from django.shortcuts
    if request.method == "POST":
        id = request.POST.get('id')
        if id:
            problem_on_update = Problem.objects.get(id=id)
            problem_on_update.reverse_and_save()
        return redirect('/')

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
    