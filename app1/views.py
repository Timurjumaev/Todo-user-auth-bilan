from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Reja.objects.create(
                nom=request.POST.get('sarlavha'),
                sana=request.POST.get('muddat'),
                batafsil=request.POST.get('batafsil'),
                holat=request.POST.get('holat'),
                student= Student.objects.get(user=request.user)
            )
            return redirect('/plans/')
        data={
            'rejalar': Reja.objects.filter(student__user=request.user)
        }
        return render(request, 'todo.html', data)
    else:
        return redirect('/')



def delete(request, son):
    if request.user == Reja.objects.get(id=son).student.user:
        if Reja.objects.get(id=son).delete():
            return redirect('/plans/')
    else:
        return redirect('/plans/')




def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/plans/')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        u=User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')

        )
        Student.objects.create(
            fullname=request.POST.get('fl'),
            guruh=request.POST.get('fl'),
            st_raqam=request.POST.get('fl'),
            tel=request.POST.get('fl'),
            user=u
        )
        return redirect('/')
    return render(request, 'register.html')





