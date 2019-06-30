from rest_framework import serializers
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
        fields = ('section', 'date_subscribed', 'active', 'premium')

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.customUser
        fields = ('email', 'sections')
        