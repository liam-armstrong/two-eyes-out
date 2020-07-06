from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models

class sectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.section
        fields = ('dept', 'code', 'sect')
    
    def create(self, req, instance=None):
        assert instance is None, 'Cannot update section from a serializer'
        section_object = models.section.objects.get_or_create(
            dept = req.get('dept'),
            code = req.get('code'),
            sect = req.get('sect')
        )
        return section_object
    
    def get(self, req):
        section_object = models.section.objects.get(
            dept = req.get('dept'),
            code = req.get('code'),
            sect = req.get('sect')
        )
        return section_object

    def get_unique_together_validators(self):
        return []

class subscriptionSerializer(serializers.ModelSerializer):
    section = sectionSerializer()

    class Meta:
        model = models.subscription
        fields = ('id', 'section', 'active', 'premium')

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.customUser
        fields = '__all__'

    def create(self, req, instance=None):
        assert instance is None, 'Cannot update user from a serializer'
        UserModel = get_user_model()
        return UserModel.objects.create_user(email = req.get('email'), password = req.get('password'))
        