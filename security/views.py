from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse 

# Create your views here.


def register(request):
    if request.method == "post":
        form = UserCreationForm(request, request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created {username}")
            login(request, user)
            messages.info(request, f"tu es maintenant connecté en tant que {username}")
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")
    form = UserCreationForm
    return render(request, 'security/register.html', context={"form":form})


def login_request(request):
    if request.method == "post":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalide username or password")
        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm
    return render(request, 'security/login.html', context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Successfully disconnected")
    return redirect('/')
