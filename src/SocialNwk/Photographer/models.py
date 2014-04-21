from django.db import models
from django.contrib.auth.models import User
from time import strftime, gmtime

import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4().hex, ext)
    return os.path.join('uploads/', strftime('%Y%m%d', gmtime()),  filename)


class Work(models.Model):
    author = models.ForeignKey(User, related_name='works')
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=get_file_path)
    upload_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_time']


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profiles')
    about = models.CharField(max_length=200, default='This guy is to lazy to introduce him/her self')
    follows = models.ManyToManyField('UserProfile', related_name='followers', symmetrical=False)

    def __unicode__(self):
        return self.user.id

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])