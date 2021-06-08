from django.urls import path

from .views import ( HomePageView,
                     EventListView,
                     EventCreateView,
                     EventUpdateView,
                     EventDetailView,
                     EventDeleteView,
                     AssetListView)
urlpatterns = [
    # path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='events'),
    path('assets/', AssetListView.as_view(), name='Assets_list'),
    path('new/', EventCreateView.as_view(), name='event_new'),
    path('<pk>/edit/', EventUpdateView.as_view(), name='event_edit'), # new
    path('<pk>/',EventDetailView.as_view(), name='event_detail'), # new
    path('<pk>/delete/',EventDeleteView.as_view(), name='event_delete'), # new
]
