from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    strength = serializers.IntegerField()
    agility = serializers.IntegerField()
    intelligence = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Character.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.strength = validated_data.get('strength', instance.strength)
        instance.agility = validated_data.get('agility', instance.agility)
        instance.intelligence = validated_data.get('intelligence', instance.intelligence)
        instance.save()
        return instance
    
