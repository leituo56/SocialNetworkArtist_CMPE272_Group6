__author__ = 'leituo56'
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SocialNwk.settings'
from django.conf import settings
from Photographer.models import *
import random

users = []
for i in range(100):
    username = 'test_user' + str(i)
    temp, c = User.objects.get_or_create(username=username)
    temp.set_password(username)
    temp.save()
    users.append(temp)

uname = users
make = ['Canon', 'Nikon', 'Olympas']
model = ['400D', 'D50']
exposure_time = [0.0001, 10]
fnumber = [2, 10]
focal_length = [20, 150]
iso = [100, 8000]
for i in range(1000):
    p = []
    temp = Work(author=random.choice(uname), title='My Pic Title '+str(i), file='init/' + str(i % 12) + '.jpg',
                make=random.choice(make), model=random.choice(model),
                exposure_time=random.choice(exposure_time), fnumber=random.choice(fnumber),
                focal_length=random.choice(focal_length), iso=random.choice(iso),
                processing_software='Photoshop')
    temp.save()
    p.append(temp)
for i in range(99):
    users[i].profile.follows.add(users[i+1].profile)