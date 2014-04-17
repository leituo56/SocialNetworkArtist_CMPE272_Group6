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
    author = models.ForeignKey(User, related_name='Works')
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=get_file_path)
    upload_time = models.DateTimeField(auto_now_add=True)
