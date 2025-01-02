from django.shortcuts import render,HttpResponse
from .models import *
from .forms import *

# Create your views here.

# crud_operations...

# display the form to user and enter the data and stores in our db:
# create ..
def create(request):
    data=studentform()
    if request.method=='POST':
        data1=studentform(request.POST)
        if data1.is_valid():
            data1.save()
            return HttpResponse('<h2> successfully stored </h2>')
    return render(request,'form.html',{'data':data})


# display....
def display(request):
    data=student.objects.all()
    return render(request,'index.html',{'data':data})



# delete...
def delete(request,id):
    data=student.objects.get(id=id)
    data.delete()
    data=student.objects.all()
    return render(request,'index.html',{'data':data})

# update:
def update(request,id):
    data=student.objects.get(id=id)
    if request.method=='POST':
        data.name=request.POST.get('name')
        data.subject=request.POST.get('subject')
        data.marks=request.POST.get('marks')
        data.save()
        data2=student.objects.all()
        return render(request,'index.html',{'data':data2})
    return render(request,'update.html',{'data':data})





