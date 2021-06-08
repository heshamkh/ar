from django.urls import path

from .views import ( HomePageView,
                     EventListView,
                     EventCreateView,
                     EventUpdateView,
                     EventDetailView,
                     EventDeleteView,
                     AssetListView,
                     AssetCreateView,
                     AssetUpdateView,
                     AssetDetailView,
                     AssetDeleteView,)
urlpatterns = [
    # path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='events'),
    path('assets/', AssetListView.as_view(), name='Assets_list'),
    path('new_event/', EventCreateView.as_view(), name='event_new'),
    path('<pk>/edit_event/', EventUpdateView.as_view(), name='event_edit'),
    path('<pk>/event_details', EventDetailView.as_view(), name='event_detail'),
    path('<pk>/delete_event', EventDeleteView.as_view(), name='event_delete'),
    path('new_asset/', AssetCreateView.as_view(), name='Asset_new'),
    path('<pk>/edit_asset/', AssetUpdateView.as_view(), name='Asset_edit'),
    path('<pk>/assets_details', AssetDetailView.as_view(), name='Asset_detail'),
    path('<pk>/delete_asset/',AssetDeleteView.as_view(), name='Asset_delete'),
]
