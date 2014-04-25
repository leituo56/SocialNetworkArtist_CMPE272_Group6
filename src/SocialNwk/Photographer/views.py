from django.shortcuts import render, redirect, get_object_or_404
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
    # work_list = Work.objects.all().order_by('-upload_time')
    if request.user.is_authenticated():
        return redirect(reverse('photo:feed'))
        # user_list = User.objects.all()
        # return render(request, 'index.html', {'user_list': user_list, 'work_list': work_list})
    else:
        return redirect(reverse('photo:explore'))
        # return render(request, 'index.html', {'work_list': work_list})


@ensure_csrf_cookie
def explore(request):
    return render(request, 'explore.html')


@ensure_csrf_cookie
def feed(request):
    if not request.user.is_authenticated():
        return redirect(reverse('photo:login'))
    return render(request, 'feed.html')


@ensure_csrf_cookie
def photo_page(request, pk):
    work = get_object_or_404(Work, pk=pk)
    author = work.author
    user = request.user
    followed = False
    if user.is_authenticated():
        lists = [item['user'] for item in user.profile.follows.values('user')]
        followed = author.id in lists
    me = int(author.id)==int(request.user.id)
    return render(request, 'photo_page.html', {'pk': pk, 'followed': followed, 'author': author.id, 'me': me})


@ensure_csrf_cookie
def user_page(request, pk):
    user = get_object_or_404(User, pk=pk)
    followed = False
    if request.user.is_authenticated():
        lists = [item['user'] for item in request.user.profile.follows.values('user')]
        followed = int(pk) in lists
        print pk, lists, followed
    me = int(pk)==int(request.user.id)
    return render(request, 'user_page.html', {'pk': pk, 'followed': followed, 'user_data': user, 'me': me})


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


# Follow a user
@api_view(['GET', 'POST', ])
def follow(request, pk, format=None):
    user = request.user
    target = get_object_or_404(User, pk=pk)
    if not user.is_authenticated() and target:
        return redirect(reverse('photo:login'))
    user.profile.follows.add(target.profile)
    return Response(data={'success': 1})

# Unfollow a user
@api_view(['GET', 'POST', ])
def unfollow(request, pk, format=None):
    user = request.user
    target = get_object_or_404(User, pk=pk)
    if not user.is_authenticated() and target:
        return redirect(reverse('photo:login'))
    user.profile.follows.remove(target.profile)
    return Response(data={'success': 1})

# API root
@api_view(('GET',))
def api_root(request, format=None):
    return Response(
        {
            'users': rest_framework.reverse.reverse('photo:user-list', request=request),
            'photos': rest_framework.reverse.reverse('photo:photo-list', request=request),
            'follow someone': 'example: /api/users/1/follow',
            'unfollow someone': 'example: /api/users/1/unfollow',
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

        # Return photos uploaded by authenticated user
        me = self.request.QUERY_PARAMS.get('me', None)
        if me is not None and self.request.user.is_authenticated():
            queryset = queryset.filter(author=user)

        # Return photos uploaded by followers
        feed = self.request.QUERY_PARAMS.get('feed', None)
        if feed is not None and self.request.user.is_authenticated():
            lists = [item['user'] for item in user.profile.follows.values('user')]
            queryset = queryset.filter(author__in=lists)
        return queryset

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    def pre_save(self, obj):
        obj.author = self.request.user

    queryset = Work.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


