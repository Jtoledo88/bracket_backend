from rest_framework import serializers
from .models import Service, Event

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'title', 'description')
		model = Service

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'title', 'description', 'author', 'day', 'timing')
		model = Event