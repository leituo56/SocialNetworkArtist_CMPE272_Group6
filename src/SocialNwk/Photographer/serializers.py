from rest_framework import serializers
from django.contrib.auth.models import User
from Photographer.models import Work
import rest_framework


class UserSerializer(serializers.HyperlinkedModelSerializer):
    works = serializers.HyperlinkedRelatedField(many=True, view_name='photo:photo-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='photo:user-detail')
    follows = serializers.Field(source='profile.follows.all.values')
    followers = serializers.Field(source='profile.followers.all.values')

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'works', 'follows', 'followers')

        #depth = 1


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    #author = serializers.Field(source='author.id')
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    authorName = serializers.Field(source='author.username')
    #author = serializers.RelatedField()
    url = serializers.HyperlinkedIdentityField(view_name='photo:photo-detail')

    def transform_file(self, obj, value):
        if obj is not None:
            return obj.file.url
        return value

    class Meta:
        model = Work
        fields = ('url', 'id', 'author', 'authorName',
                  'title', 'file', 'upload_time')
        #depth = 1