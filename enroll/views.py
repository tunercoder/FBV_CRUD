from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    if request.method =="POST":
        fm =StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            age=fm.cleaned_data['age']
            roll=fm.cleaned_data['roll']
            standard=fm.cleaned_data['standard']
            st=Student(name=name,age=age,roll=roll,standard=standard)
            st.save()
            #or
            # fm.save()
            fm =StudentForm()
    else:
        fm =StudentForm()
    students=Student.objects.all()
    return render(request,'enroll/addandshow.html',{'form': fm,'students':students})

def update_student(request,id):
    student=Student.objects.get(pk=id)
    if request.method =="POST":
        fm =StudentForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/enroll/') 
    else:
        fm =StudentForm(instance=student)
    return render(request,'enroll/update.html',{'form': fm})


def delete_student(request,id):
    if request.method =="POST":
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect('/enroll/') 
