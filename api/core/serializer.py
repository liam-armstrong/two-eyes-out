from rest_framework import serializers
from . import models

class sectionSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = models.section
        fields = ('dept', 'code', 'sect', 'is_active')
    
    def create(self, attrs, instance=None):
        assert instance is None, 'Cannot update section from a serializer'
        section_object = models.section.objects.get_or_create(
            dept = attrs.get('dept'),
            code = attrs.get('code'),
            sect = attrs.get('sect')
        )

        return section_object
    
    def get(self, attrs):
        section_object = models.section.objects.get(
            dept = attrs.get('dept'),
            code = attrs.get('code'),
            sect = attrs.get('sect')
        )

        return section_object

    def get_unique_together_validators(self):
        return []

    def get_is_active(self, obj):
        is_active = self.context.get('is_active')
        return is_active

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.customUser
        fields = ('email', 'sections')
        