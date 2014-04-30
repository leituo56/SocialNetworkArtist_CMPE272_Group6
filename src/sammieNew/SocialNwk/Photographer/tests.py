from django.test import TestCase
from Photographer.models import *
import random


# Create your tests here.
class MyTest(TestCase):

    def test_case_a(self):
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

    def test_case_b(self):
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