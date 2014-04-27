from django.db import models
from django.contrib.auth.models import User
from time import strftime, gmtime
from django.db.models import Count, Avg
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4().hex, ext)
    return os.path.join('uploads/', strftime('%Y%m%d', gmtime()),  filename)


class Work(models.Model):
    #Basic Info
    author = models.ForeignKey(User, related_name='works')
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=get_file_path)
    upload_time = models.DateTimeField(auto_now_add=True)

    #EXIF data
    make = models.CharField(max_length=50, default='Undefined', blank=True)
    model = models.CharField(max_length=100, default='Undefined', blank=True)
    exposure_time = models.FloatField(default=1.0)
    fnumber = models.FloatField(default=4.0)
    focal_length = models.FloatField(default=50.0)
    iso = models.PositiveIntegerField(default=100)
    processing_software = models.CharField(max_length=100, default='None', blank=True)

    #lens_make = models.CharField(max_length=50, default='Undefined', blank=True)
    #lens_model = models.CharField(max_length=100, default='Undefined', blank=True)

    #Photo Feature
    portrait = models.BooleanField(default=False, blank=True)
    landscape = models.BooleanField(default=False, blank=True)
    telephoto = models.BooleanField(default=False, blank=True)
    low_light = models.BooleanField(default=False, blank=True)
    high_speed = models.BooleanField(default=False, blank=True)
    long_exposure = models.BooleanField(default=False, blank=True)

    def save(self,  *args, **kwargs):
        self.portrait = 0 < self.fnumber < 2.8 and self.focal_length > 50
        self.landscape = 0 < self.focal_length < 35
        self.telephoto = self.focal_length > 135
        self.low_light = self.iso > 6400
        self.high_speed = 0 < self.exposure_time < 0.001
        self.long_exposure = self.exposure_time > 8
        super(Work, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id) + ',' + str(self.title)

    class Meta:
        ordering = ['-upload_time']


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profiles')
    about = models.CharField(max_length=200, default='This guy is to lazy to introduce him/her self')
    follows = models.ManyToManyField('UserProfile', related_name='followers', symmetrical=False)

    def __unicode__(self):
        return self.user.id

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])