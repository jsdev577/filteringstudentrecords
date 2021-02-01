from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student

def index(request):

    student=StudentForm()
    student1=Student.objects.all()
    if request.method=='POST':
        student=StudentForm(request.POST)
        if student.is_valid():
            student.save()
            return redirect('/')
    data={'student':student,'student1':student1}
    return render(request,"student/index.html",data)

def delete(request, pk):
    student=Student.objects.get(id=pk)
    if request.method =='GET':
        student.delete()
        return redirect('/')
    context={'form':student}
    return render (request,'student/index.html', context)
