from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import GeeksModel
from .forms import GeeksForm

# To create a particular view
def create_view(request):
    # return HttpResponse('<h1> Hello </h1>')
    context = {}
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,"create_view.html",context)

def list_view(request):
    context = {}
    context['dataset'] = GeeksModel.objects.all()
    return render(request,'list_view.html',context)

def detail_view(request,id):
    context = {}
    context['data'] = GeeksModel.objects.get(id=id)
    return render(request,'detail_view.html',context)

# Update view

from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)

def update_view(request,id):
    context = {}
    obj = get_object_or_404(GeeksModel,id=id)
    form = GeeksForm(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/geekapi/'+id)
    context['form'] = form

    return render(request,"update_view.html",context)

def delete_view(request,id):
    context = {}
    object = get_object_or_404(GeeksModel,id=id)
    if request.method=='POST':
        object.delete()
        return HttpResponseRedirect('/geekapi')
    return render(request,'delete_view.html',context)