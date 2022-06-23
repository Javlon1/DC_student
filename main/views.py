from django.shortcuts import render,redirect
from main.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def Index(request):
    context = {
    'students':Student.objects.all().order_by('-id'),
    'i':Info.objects.last()
    }
    return render(request, 'home.html',context)


@login_required
def InfoView(request):
    info = Info.objects.all()
    context = {
    'info': info,
    'i':Info.objects.last()
    }
    return render(request, 'info.html',context)


@login_required
def HomeView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    context = {
    'students':Student.objects.all().order_by('-id'),
    'i':Info.objects.last()
    }

    return render(request, 'index.html',context)


@login_required
def StudentCreate(request):
    student = Student.objects.all().order_by('-id')
    context = {
        "student": student,
        'i':Info.objects.last()
    }
    if request.method == "POST":
        data = request.POST
        Student.objects.create(
            name=data.get('name'),
            surname=data.get('surname'),
            age=data.get('age'),
            address=data.get('address'),
            studyed=data.get('studyed'),
            job=data.get('job'),
        )
        return redirect('home')
    return render(request, 'create.html', context)


@login_required
def InfoCreate(request):
    context = {
        'i':Info.objects.last()
    }
    if request.method == "POST" and request.FILES:
        logo = request.FILES['logo']
        img = request.FILES['img']
        Info.objects.create(logo=logo,img=img)
        return redirect('home')
    return render(request, 'info_create.html', context)


@login_required
def StudentEdit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student = Student.objects.get(id=pk)
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.age = request.POST.get('age')
        student.address = request.POST.get('address')
        student.studyed = request.POST.get('studyed')
        student.job = request.POST.get('job')
        student.save()
        return redirect('home')
    context = {
        "student": student,
        'i':Info.objects.last()
    }
    return render(request, 'edit.html', context)

@login_required
def InfoEdit(request, pk):
    info = Info.objects.get(id=pk)
    if request.method == "POST":
        info = Info.objects.get(id=pk)
        if 'logo' in request.FILES:
            info.logo = request.FILES['logo']
        if 'img' in request.FILES:
            info.img = request.FILES['img']
        info.save()
        return redirect('info')
    context = {
        "info": info,
        'i':Info.objects.last()
    }
    return render(request, 'infoedit.html', context)

@login_required
def InfoDelete(request, pk):
    context = {
        'info':Info.objects.last()
    }
    info = Info.objects.get(id=pk)
    info.delete()
    return redirect('info')


@login_required
def StudentDelete(request, pk):
    context = {
        'info':Info.objects.last()
    }
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('home')


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username =request.POST.get("username")
        password = request.POST.get ('password')
        employe = User.objects.filter(username=username)
        if employe.count() > 0:
            if employe[0].check_password(password):
                login(request,employe[0])
                return redirect("home")
            else:
                return redirect('login')
        else:
            return redirect('login')    
    return render(request, 'login.html')

