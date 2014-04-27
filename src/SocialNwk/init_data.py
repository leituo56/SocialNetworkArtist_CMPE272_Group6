__author__ = 'leituo56'
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SocialNwk.settings'
from django.conf import settings
from Photographer.models import *
import random

tuolei, c = User.objects.get_or_create(username='tuolei')
tuolei.set_password('tuolei')
xiaolijiang, c = User.objects.get_or_create(username='xiaolijiang')
xiaolijiang.set_password('xiaolijiang')
wenjiazhang, c = User.objects.get_or_create(username='wenjiazhang')
wenjiazhang.set_password('wenjiazhang')
tuolei.save()
wenjiazhang.save()
xiaolijiang.save()

uname = [tuolei, xiaolijiang, wenjiazhang]
make = ['Canon', 'Nikon', 'Olympas']
model = ['400D', 'D50']
exposure_time = [0.0001, 10]
fnumber = [2, 10]
focal_length = [20, 150]
iso = [100, 8000]
for i in range(12):
    p = []
    temp = Work(author=random.choice(uname), title='My Pic'+str(i), file='init/' + str(i) + '.jpg',
                make=random.choice(make), model=random.choice(model),
                exposure_time=random.choice(exposure_time), fnumber=random.choice(fnumber),
                focal_length=random.choice(focal_length), iso=random.choice(iso),
                processing_software='Photoshop')
    temp.save()
    p.append(temp)
tuolei.profile.follows.add(xiaolijiang.profile)
xiaolijiang.profile.follows.add(wenjiazhang.profile)
wenjiazhang.profile.follows.add(tuolei.profile)