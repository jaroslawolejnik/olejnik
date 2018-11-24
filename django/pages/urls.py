from django.urls import path

from .views import AboutPageView, HomePageView, PodstronaPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('podstrona/', PodstronaPageView.as_view(), name='podstrona'),
]
