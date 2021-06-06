from django.urls import path

from .views import HomePageView , EventListView, EventCreateView

urlpatterns = [
    # path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='events'),
    path('new/', EventCreateView.as_view(), name='event_new'),
]