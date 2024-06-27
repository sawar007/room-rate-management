from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Discount, DiscountRoomRate, OverriddenRoomRate, RoomRate
from .serializers import DiscountRoomRateSerializer, DiscountSerializer, OverriddenRoomRateSerializer, \
    RoomRateSerializer


class RoomRateViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given room rate.

    list:
    Return a list of all the existing room rates.

    create:
    Create a new room rate.

    update:
    Update an existing room rate.

    partial_update:
    Partially update an existing room rate.

    destroy:
    Delete an existing room rate.
    """
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer


class OverriddenRoomRateViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given overridden room rate.

    list:
    Return a list of all the existing overridden room rates.

    create:
    Create a new overridden room rate.

    update:
    Update an existing overridden room rate.

    partial_update:
    Partially update an existing overridden room rate.

    destroy:
    Delete an existing overridden room rate.
    """
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given discount.

    list:
    Return a list of all the existing discounts.

    create:
    Create a new discount.

    update:
    Update an existing discount.

    partial_update:
    Partially update an existing discount.

    destroy:
    Delete an existing discount.
    """
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountRoomRateViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given discount-room rate mapping.

    list:
    Return a list of all the existing discount-room rate mappings.

    create:
    Create a new discount-room rate mapping.

    update:
    Update an existing discount-room rate mapping.

    partial_update:
    Partially update an existing discount-room rate mapping.

    destroy:
    Delete an existing discount-room rate mapping.
    """
    queryset = DiscountRoomRate.objects.all()
    serializer_class = DiscountRoomRateSerializer


class LowestRatesView(APIView):
    """
    get:
    Return the lowest rates for a specific room and date range.
    """

    def get(self, request, room_name, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        try:
            room_rate = RoomRate.objects.get(room_name=room_name)
        except RoomRate.DoesNotExist:
            return Response({"error": "Room not found"}, status=404)

        rates = {}
        current_date = start_date

        while current_date <= end_date:
            rates[str(current_date)] = room_rate.get_final_rate(current_date)
            current_date += timedelta(days=1)

        return Response(rates)
