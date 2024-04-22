from django.urls import path
from .views import freelancer_profile

urlpatterns = [
    path('profile/<int:id>/', freelancer_profile, name='freelancer_profile'),
]