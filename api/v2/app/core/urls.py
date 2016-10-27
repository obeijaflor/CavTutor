"""isa_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
#from django.contrib import admin

from rest_framework import routers
from CavTutor import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'institutions', views.InstitutionViewSet)
router.register(r'tutors', views.TutorViewSet)
router.register(r'tutees', views.TuteeViewSet)
router.register(r'courses', views.CourseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/v2/', include(router.urls)),
    url(r'^api/v2/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
