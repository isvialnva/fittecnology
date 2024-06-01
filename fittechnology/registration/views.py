from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, "registration/register.html", {'form': UserCreationForm})
    else:
        if request.POST["password1"] != request.POST["password2"]:
            return render(request, "registration/register.html",
                          {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden, corrígelas'})
        else:
            name = request.POST["username"]
            pasw = request.POST["password1"]
            user = User.objects.create_user(username=name, password=pasw)
            user.save()
            return render(request, "registration/login.html", {'mensaje': 'Usuario registrado'})
