from rest_framework import serializers
from . import models

class sectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.section
        fields = ('dept', 'code', 'sect')

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.customUser
        fields = ('email', 'sections')