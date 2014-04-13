from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from datetime import datetime
from Photographer.forms import DocumentForm
from Photographer.models import *


def test(request):
    return render(request, 'test.html')


def home(request):
    work_list = Work.objects.all()
    if request.user.is_authenticated():
        user_list = User.objects.all()
        return render(request, 'index.html', {'user_list': user_list, 'work_list': work_list})
    else:
        return render(request, 'index.html', {'work_list': work_list})


def signup(request):
    if request.method == 'POST':  # POST
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Success
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('photo:home'))  # Redirect to a success page.
        else:  # Not Success
            return render(request, "registration/signup.html", {'form': form})
    else:  # GET
        form = UserCreationForm()
        return render(request, "registration/signup.html", {'form': form})  # Signup Page


def login_view(request):
    if request.method == 'POST':  # POST
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('photo:home'))  # Redirect to a success page.
        else:
            error_msg = 'Wrong User or Password!!!'
            return render(request, 'registration/login.html', {'error': error_msg})  # Return with error Msg
    else:  # GET
        return render(request, 'registration/login.html')  # Login Page


def logout_view(request):
    logout(request)
    return redirect(reverse('photo:home'))


def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Work(author=request.user, title=form.cleaned_data['title'], file=request.FILES['file'],
                          upload_time=datetime.now())
            newdoc.save()
            # Redirect to the home after POST
            return redirect(reverse('photo:home'))
    else:
        form = DocumentForm()  # A empty, unbound form
    return render(request, 'upload.html', {'form': form})



