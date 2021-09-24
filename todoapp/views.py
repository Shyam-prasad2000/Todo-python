
from django.shortcuts import render, redirect
from . models import Task as task
from . forms import Todoforms
# Create your views herd
def taskview(request):
    obj1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=task.objects.create(name=name,priority=priority,date=date)
        obj.save()

    return render(request,'taskview.html',{'obj1':obj1})

def delete(request,taskid):

    value=task.objects.get(id=taskid)
    if request.method=="POST":
        value.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':value})


def update(request,id):
    value=task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=value)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':value,'form':form})