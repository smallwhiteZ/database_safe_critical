from django.http import HttpResponse
from django.template import loader
from .models import Scene,report

def members(request):
  mymembers = Scene.objects.all().values()
  template = loader.get_template('all_scenes.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Scene.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def report_details(request,id):
  mymember = report.objects.filter(scenename_id=id).values()
  template = loader.get_template('reports.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def reports(request,id):
  mymember = report.objects.get(id=id)
  template = loader.get_template('report_details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def all_reports(request):
  mymembers = report.objects.all().values()
  template = loader.get_template('all_reports.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))