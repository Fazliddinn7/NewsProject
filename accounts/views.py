from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def userLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Welcome to registration')
                else:
                    return HttpResponse("Account not found")
            else:
                return HttpResponse('Login yoki passwordda xatolik bor')
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/login.html', context)


