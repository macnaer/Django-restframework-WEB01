from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContactListSerializer


class ContactListSerializerViewSet(viewsets.ModelViewSet):
    contact_list = ContactListSerializer.objects().all()
    serializer_class = ContactListSerializer
    print(contact_list)
