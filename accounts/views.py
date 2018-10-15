from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import StudentLoginForm
from django.contrib.auth.decorators import login_required

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, 'accounts/login_success.html')
        else:
            return HttpResponse('Invalid credentials')
    else:
        student_login_form = StudentLoginForm()
        print('GET request')
        return render(request, 'accounts/login.html', {
        'student_login_form': student_login_form
        })

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
