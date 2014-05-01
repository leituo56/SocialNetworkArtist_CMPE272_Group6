from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models import signals
from time import strftime, gmtime
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

    #Photo Category
    portrait = models.BooleanField(default=False, blank=True)
    landscape = models.BooleanField(default=False, blank=True)
    telephoto = models.BooleanField(default=False, blank=True)
    low_light = models.BooleanField(default=False, blank=True)
    high_speed = models.BooleanField(default=False, blank=True)
    long_exposure = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
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


# Work's post_save()
def create_photo(sender, instance, created, **kwargs):
    queryset = instance.author.works
    result = get_stat(queryset=queryset)
    instance.author.profile.save(result=result)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profiles')
    about = models.CharField(max_length=200, default='This guy is to lazy to introduce him/her self')
    follows = models.ManyToManyField('UserProfile', related_name='followers', symmetrical=False)

    fav_make = models.CharField(max_length=100, default='', blank=True)
    fav_model = models.CharField(max_length=100, default='', blank=True)
    fav_category = models.CharField(max_length=100, default='', blank=True)

    def save(self, result=None, *args, **kwargs):
        if result is not None:
            self.fav_make = result['fav_make']
            self.fav_model = result['fav_model']
            self.fav_category = result['fav_category']
        super(UserProfile, self).save(*args, **kwargs)

    def raw_data(self):
        return {
            'user': self.user.id,
        }

    def __unicode__(self):
        return self.user.id

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
signals.post_save.connect(create_photo, sender=Work)


# Generic function for get statistics
def get_stat(queryset):
    total = queryset.count()
    f = lambda x: x != '' and x != 'Undefined' and x is not None
    p = lambda x: 0 if total == 0 else float(x) / total

    camera_make = queryset.values('make').order_by().annotate(count=Count('make')).order_by('-count')
    camera_model = queryset.values('model').order_by().annotate(count=Count('model')).order_by('-count')
    portrait_pct = p(queryset.filter(portrait=True).count())
    landscape_pct = p(queryset.filter(landscape=True).count())
    telephoto_pct = p(queryset.filter(telephoto=True).count())
    low_light_pct = p(queryset.filter(low_light=True).count())
    high_speed_pct = p(queryset.filter(high_speed=True).count())
    long_exposure_pct = p(queryset.filter(long_exposure=True).count())

    make_stat = [{'make': item['make'], 'count': item['count'], 'pct': p(item['count'])} for item in camera_make
                 if f(item["make"])][:100]
    model_stat = [{'model': item['model'], 'count': item['count'], 'pct': p(item['count'])} for item in camera_model
                  if f(item["model"])][:100]
    temp_list = [{'name': 'portrait', 'pct': portrait_pct},
                 {'name': 'landscape', 'pct': landscape_pct},
                 {'name': 'telephoto', 'pct': telephoto_pct},
                 {'name': 'low_light', 'pct': low_light_pct},
                 {'name': 'high_speed', 'pct': high_speed_pct},
                 {'name': 'long_exposure', 'pct': long_exposure_pct}]
    category_stat = sorted(temp_list, key=lambda k: k['pct'], reverse=True)
    fav_make = make_stat[0]['make'] if len(make_stat) else ''
    fav_model = model_stat[0]['model'] if len(model_stat) else ''
    fav_category = category_stat[0]['name'] if len(category_stat) and category_stat[0]['pct'] > 0 else ''
    return {
        'total': total,
        'make_stat': make_stat,
        'model_stat': model_stat,
        'category_stat': category_stat,
        'fav_make': fav_make,
        'fav_model': fav_model,
        'fav_category': fav_category,
    }

class Comment(models.Model):
    #Basic Info
    author = models.ForeignKey(User, related_name='comments')
    work = models.ForeignKey(Work, related_name='comments')
    content = models.CharField(max_length=50, default='Undefined', blank=True)

# class Comment(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(max_length=60)
#     body = models.TextField()
#     post = models.ForeignKey(Post)

#     def __unicode__(self):
#         return unicode("%s: %s" % (self.post, self.body[:60]))

# class CommentAdmin(admin.ModelAdmin):
#     display_fields = ["post", "author", "created"]

# admin.site.register(Comment, CommentAdmin)