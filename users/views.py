from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile


def userregister(request):
    if request.user.is_authenticated:
        return redirect('weight-dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'Account created for {form.cleaned_data["username"]}')
                return redirect('login')

        return render(request, "users/register.html", {'form': form})


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('weight-dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('weight-dashboard')
            else:
                messages.info(request, 'Username or password incorrect')
                return redirect('login')

        return render(request, "users/login.html")


def userlogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('weight-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "users/profile.html", {"title": "Profile", "pagename": "Profile", "u_form": u_form, "p_form": p_form})