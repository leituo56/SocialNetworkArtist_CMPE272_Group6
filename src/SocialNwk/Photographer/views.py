from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from datetime import datetime
from Photographer.forms import DocumentForm
from Photographer.models import *
from Photographer.serializers import *
from Photographer.permissions import *
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import renderers
import rest_framework.reverse


@ensure_csrf_cookie
def test(request):
    return render(request, 'test.html')


@ensure_csrf_cookie
def home(request):
    work_list = Work.objects.all().order_by('-upload_time')
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
    if not request.user.is_authenticated():
        return redirect(reverse('photo:login'))
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Work(author=request.user, title=form.cleaned_data['title'], file=request.FILES['file'])
            #upload_time=datetime.now())
            newdoc.save()
            # Redirect to the home after POST
            return redirect(reverse('photo:home'))
    else:
        form = DocumentForm()  # A empty, unbound form
    return render(request, 'upload.html', {'form': form})


@api_view(('GET',))
def api_root(request, format=None):
    return Response(
        {
            'users': rest_framework.reverse.reverse('photo:user-list', request=request),
            'photos': rest_framework.reverse.reverse('photo:photo-list', request=request),
        }
    )


class UserList(generics.ListAPIView):
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoList(generics.ListCreateAPIView):
    def pre_save(self, obj):
        obj.author = self.request.user

    serializer_class = PhotoSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    ordering = ('-upload_time',)
    filter_fields = ('id', 'author', 'title', 'make',
                     'portrait', 'landscape', 'telephoto', 'low_light', 'high_speed', 'long_exposure')

    def get_queryset(self):
        queryset = Work.objects.all()
        user = self.request.user
        me = self.request.QUERY_PARAMS.get('me', None)
        if me is not None and self.request.user.is_authenticated():
            queryset = queryset.filter(author=user)
        return queryset

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    def pre_save(self, obj):
        obj.author = self.request.user

    queryset = Work.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


