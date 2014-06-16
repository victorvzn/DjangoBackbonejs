#encoding:utf-8
from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializers import ContactSerializer


class HomeTemplateView(TemplateView):

    template_name = 'home.html'


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)