from rest_framework import serializers
from django.contrib.auth.models import User
from Photographer.models import Work
import rest_framework


class UserSerializer(serializers.HyperlinkedModelSerializer):
    works = serializers.HyperlinkedRelatedField(many=True, view_name='photo:photo-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='photo:user-detail')
    follows = serializers.Field(source='profile.follows.all.values')
    followers = serializers.Field(source='profile.followers.all.values')
    is_follow = serializers.SerializerMethodField('is_follow_already')

    def is_follow_already(self, obj):
        user = self.context['request'].user
        if user.is_authenticated():
            lists = [item['user'] for item in user.profile.follows.values('user')]
            return obj.id in lists
        return False

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'works', 'follows', 'followers', 'is_follow')
        #depth = 1


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    #author = serializers.RelatedField()
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    authorName = serializers.Field(source='author.username')
    url = serializers.HyperlinkedIdentityField(view_name='photo:photo-detail')

    portrait = serializers.Field(source='portrait')
    landscape = serializers.Field(source='landscape')
    telephoto = serializers.Field(source='telephoto')
    low_light = serializers.Field(source='low_light')
    high_speed = serializers.Field(source='high_speed')
    long_exposure = serializers.Field(source='long_exposure')

    def transform_file(self, obj, value):
        if obj is not None:
            return obj.file.url
        return value

    class Meta:
        model = Work
        fields = ('url', 'id', 'author', 'authorName',
                  'title', 'file', 'upload_time', 'make', 'model', 'exposure_time',
                  'fnumber', 'focal_length', 'iso', 'processing_software',
                  'portrait', 'landscape', 'telephoto', 'low_light', 'high_speed', 'long_exposure')
        #depth = 1