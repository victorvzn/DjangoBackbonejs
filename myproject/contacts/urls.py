from django.conf.urls import patterns, include, url

from .views import HomeTemplateView, ContactViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = patterns('',

    url(r'^$', HomeTemplateView.as_view(), name='home'),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)