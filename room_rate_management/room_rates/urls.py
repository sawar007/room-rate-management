from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DiscountRoomRateViewSet, DiscountViewSet, LowestRatesView, OverriddenRoomRateViewSet, RoomRateViewSet

router = DefaultRouter()
router.register(r'room-rates', RoomRateViewSet)
router.register(r'overridden-room-rates', OverriddenRoomRateViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'discount-room-rates', DiscountRoomRateViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('lowest-rates/<str:room_name>/<str:start_date>/<str:end_date>/', LowestRatesView.as_view(), name='lowest-rates')
]