from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            success(request , f'Welcome {username}, Your account has been created')
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request , 'users/create_user.html' , {
        'form' : form
    })

@login_required
def profile(request):
    return render(request , 'users/profile.html')
