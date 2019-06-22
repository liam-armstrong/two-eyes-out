from rest_framework import serializers
from . import models

class sectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.section
        fields = ('dept', 'code', 'sect')
    
    def create(self, attrs, instance=None):
        assert instance is None, 'Cannot update section from a serializer'
        section_object = models.section.objects.get_or_create(
            dept = attrs.get('dept'),
            code = attrs.get('code'),
            sect = attrs.get('sect')
        )

        return section_object

    def get_unique_together_validators(self):
        return []

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.customUser
        fields = ('email', 'sections')
        