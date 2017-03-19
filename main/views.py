#!C:/Users/arif/AppData/Local/Programs/Python/Python35-32/python.exe
from django.shortcuts import render_to_response
from .models import projects
def main_page(request):
    return render_to_response('main_page.html')

def portfolio(request):
    return render_to_response('portfolio.html')
def project(request):
    prjcts = projects.objects.all()
    args ={}
    args['projects'] = prjcts

    print(project)
    return render_to_response('projects.html', args)
def contacts(request):
    return  render_to_response('conpacts.html')