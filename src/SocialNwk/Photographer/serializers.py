from rest_framework import serializers
from django.contrib.auth.models import User
from Photographer.models import Work
import rest_framework


class UserSerializer(serializers.HyperlinkedModelSerializer):
    Works = serializers.HyperlinkedRelatedField(many=True, view_name='photo:photo-detail')
    url = serializers.HyperlinkedIdentityField(
        view_name='photo:user-detail'
    )

    #url = serializers.CharField('aaa')
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'Works')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.Field(source='author.id')
    authorName = serializers.Field(source='author.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    url = serializers.HyperlinkedIdentityField(
        view_name='photo:photo-detail'
    )
    fileURL = serializers.SerializerMethodField('file_url')

    def file_url(self, obj):
        return obj.file.url

    class Meta:
        model = Work
        fields = ('url', 'id', 'author', 'authorName',
                  'title', 'file', 'fileURL', 'upload_time')