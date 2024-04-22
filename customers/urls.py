from django.urls import path
from .views import customer_profile

urlpatterns = [
    path('profile/<int:id>/', customer_profile, name='customer_profile'),
]
