from rest_framework import serializers
from .models import ProfileModel, EventModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['id', 'first_name', 'last_name', 'email', 'profile_picture']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ['id', 'event_name', 'category', 'description', 'date', 'event_image']
