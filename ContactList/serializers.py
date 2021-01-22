from rest_framework import serializers
from .models import ContactListModel


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactListModel
        fields = ['id', 'name', 'surname', 'role',
                  'avatar', 'status', 'email', 'gender']
