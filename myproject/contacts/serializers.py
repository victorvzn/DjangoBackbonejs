from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        
        model = Contact
        fields = ('url', 'id', 'first_name', 'last_name', 'phone_number',)