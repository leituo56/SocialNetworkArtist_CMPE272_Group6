from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.models import Q

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


def find_friends(request):
    if not request.user.is_authenticated():
        return redirect(reverse('photo:login'))
    return render(request, 'find_friends.html')


def site_stat(request):
    return render(request, 'site_stat.html')

@ensure_csrf_cookie
def photo_page(request, pk):
    work = get_object_or_404(Work, pk=pk)
    author = work.author
    user = request.user
    followed = False
    if user.is_authenticated():
        lists = [item['user'] for item in user.profile.follows.values('user')]
        followed = author.id in lists
    me = int(author.id) == int(request.user.id) if request.user.is_authenticated() else 0
    return render(request, 'photo_page.html', {'pk': pk, 'followed': followed, 'author': author.id, 'me': me})


@ensure_csrf_cookie
def user_page(request, pk):
    user = get_object_or_404(User, pk=pk)
    followed = False
    if request.user.is_authenticated():
        lists = [item['user'] for item in request.user.profile.follows.values('user')]
        followed = int(pk) in lists
        print pk, lists, followed
    me = int(pk) == int(request.user.id) if request.user.is_authenticated() else 0
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
        return Response(data={'redirect': reverse('photo:login')})
    user.profile.follows.add(target.profile)
    return Response(data={'success': 1})


# Unfollow a user
@api_view(['GET', 'POST', ])
def unfollow(request, pk, format=None):
    user = request.user
    target = get_object_or_404(User, pk=pk)
    if not user.is_authenticated() and target:
        return Response(data={'redirect': reverse('photo:login')})
    user.profile.follows.remove(target.profile)
    return Response(data={'success': 1})


# API root
@api_view(('GET',))
def api_root(request, format=None):
    return Response(
        {
            'users': rest_framework.reverse.reverse('photo:user-list', request=request),
            'photos': rest_framework.reverse.reverse('photo:photo-list', request=request),
            'Site Statistics': rest_framework.reverse.reverse('photo:photo-stat', request=request),
            'User Statistics': 'example: /api/users/1/stat',
            'follow someone': 'example: /api/users/1/follow',
            'unfollow someone': 'example: /api/users/1/unfollow',
        }
    )


class UserList(generics.ListAPIView):
    def get_queryset(self):
        queryset = User.objects.all()
        find = self.request.QUERY_PARAMS.get('find', None)
        fav_make = self.request.QUERY_PARAMS.get('fav_make', None)
        fav_model = self.request.QUERY_PARAMS.get('fav_model', None)
        fav_category = self.request.QUERY_PARAMS.get('fav_category', None)
        if find is not None and self.request.user.is_authenticated():
            my_make = self.request.user.profile.fav_make
            my_model = self.request.user.profile.fav_model
            my_category = self.request.user.profile.fav_category
            lists = [item['user'] for item in self.request.user.profile.follows.values('user')]
            queryset = queryset.filter(Q(profiles__fav_make=my_make) | Q(profiles__fav_model=my_model)
                                       | Q(profiles__fav_category=my_category))
            # Filter off followed user
            queryset = queryset.filter(~Q(id__in=lists))
            # Filter off self
            queryset = queryset.filter(~Q(id=self.request.user.id))
            if fav_make is not None:
                queryset = queryset.filter(profiles__fav_make=my_make)
            if fav_model is not None:
                queryset = queryset.filter(profiles__fav_model=my_model)
            if fav_category is not None:
                queryset = queryset.filter(profiles__fav_category=my_category)
        return queryset

    serializer_class = UserSerializer
    filter_fields = ('username',)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(('GET',))
def user_stat(request, pk, format=None):
    target_user = get_object_or_404(User, pk=pk)
    queryset = target_user.works
    result = get_stat(queryset)
    return Response(result)


class PhotoList(generics.ListCreateAPIView):
    def pre_save(self, obj):
        obj.author = self.request.user

    serializer_class = PhotoSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    ordering = ('-upload_time',)
    filter_fields = ('id', 'author', 'title', 'make', 'model',
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


@api_view(('GET',))
def photo_stat(request, format=None):
    queryset = Work.objects.all()
    result = get_stat(queryset)
    return Response(result)

@api_view(('GET',))
def comment_list(request, pk, formal = None):
    work = get_object_or_404(Work, pk=pk)
    result = work.comments.values()

    return Response(
        {
            'result': result,
        }
    )



