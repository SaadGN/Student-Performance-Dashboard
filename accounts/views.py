from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def register(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


@login_required
def profile(request):

    return render(
        request,
        'accounts/profile.html'
    )


def user_logout(request):

    logout(request)

    return redirect('login')