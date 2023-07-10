# urls.py in your campaigns app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, DonationViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]