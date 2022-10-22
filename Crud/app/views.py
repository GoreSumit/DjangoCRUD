from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StuForm
from .models import StuReg
from django.contrib import messages

#Main Function
def show(request):
    
    if request.method =="POST":
        fm=StuForm(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['name']
           em = fm.cleaned_data['email']
           pw = fm.cleaned_data['password']
           reg=StuReg(name=nm,email=em,password=pw)
           reg.save()
           messages.success(request,'User Created successfully :{}'.format(nm))
           fm=StuForm()
    else:
        fm=StuForm()


    stud=StuReg.objects.all()
    return render(request,'index.html',{'form':fm,'data':stud})

# Delete function
def delete_data(request,id):
    if request.method == "POST":
        D = StuReg.objects.get(pk=id)
        D.delete()
        return HttpResponseRedirect('/')
#Edit function
def update_data(request,id):
    
    if request.method == "POST":
        pi=StuReg.objects.get(pk=id)
        fm=StuForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        
    else:
        pi=StuReg.objects.get(pk=id)
        fm=StuForm(instance=pi)
        
    return render(request,'update.html',{'form':fm})
