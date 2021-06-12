from django.urls import path
from .views import SignupPageView, ProfilePageView, ProfileEditPageView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('<pk>/profile_edit/', ProfileEditPageView.as_view(), name='profile_edit'),
]
