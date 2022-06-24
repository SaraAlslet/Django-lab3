from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Trainee,Course
from .forms import InsertForm
from django.views import View
from django.views.generic import UpdateView

def listtrainee(req):
    trainees=Trainee.objects.all()
    for trainee in trainees:
        print(trainee.id,trainee.name,trainee.courses)
    context = {}
    context['trainees'] = trainees
    if (req.method == 'GET'):
           return render(req, 'list.html', context)
    else:
        print(req.POST)
        return render(req, 'list.html', context)




def insert(request):
    context={}
    courses = Course.objects.all()
    context['courses'] = courses
    context['id'] = 1
    finsert = InsertForm()
    context['form'] = finsert
    if(request.method=='GET'):
        return render(request,'insert.html',context)
    else:
            finsert = InsertForm(request.POST)
            if(finsert.is_valid()):

                Trainee.objects.create(name=request.POST['name'],courses=Course.objects.get(id=request.POST['courses']),
                                       brnach=request.POST['brnach'])
                return HttpResponseRedirect('/trainee/list/')
            else:
                context['errors'] = finsert.errors
                return render(request, 'insert.html', context)

class Updategeneric(UpdateView):
    model = Trainee
    fields = '__all__'
    success_url = "/trainee/list/"

class ViewDelete(View):

    def post(self,request):
        Trainee.objects.filter(id=request.POST['id']).delete()
        return HttpResponseRedirect("/trainee/list/")




def update(request,id):

    trainee=Trainee.objects.get(id=id)
    context = {}
    context['title'] = 'Update Trainee'
    context['trainee'] = trainee
    courses = Course.objects.all()
    context['courses'] = courses
    return render(request, 'update.html', context)

def updatetrainee(request,id):
    Trainee.objects.filter(id=id).update(name=request.POST['name'],courses=Course.objects.get(id=request.POST['courses']),brnach=request.POST['brnach'])
    return HttpResponseRedirect("/trainee/list/")


def delete(request,id):
    Trainee.objects.filter(id=id).delete()
    return HttpResponseRedirect("/trainee/list/")
