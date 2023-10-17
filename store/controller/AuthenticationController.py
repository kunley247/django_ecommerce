from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from store.forms import CustomUserForm, CustomUserLoginForm

def register(request):
    form = CustomUserForm()

    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully, Login to continue")
            return redirect('/login')

    context = {'form': form}
    return render(request, "bootstrap/register.html", context)


def loginFunction(request):

    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')

    else:
        if request.method == "POST":

            usernameInput = request.POST.get('username')
            passwordInput = request.POST.get('password')

            user = authenticate(request, username = usernameInput, password = passwordInput)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged Successfully")
                return redirect('/')
            else:
                messages.success(request, "Invalid username or password")
                return redirect('/login')

        context = {'form': CustomUserLoginForm() }
        return render(request, "bootstrap/login.html", context)


def logoutFunction(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, "Logged out successfully")
        return redirect('/')
        