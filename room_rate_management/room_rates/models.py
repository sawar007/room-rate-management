# from django.db.models import SET_DEFAULT
import sys

from django.db import models

sys.path.append("..")
from django.db.models import Max


class RoomRate(models.Model):
    """
    Model representing a room rate.

    Attributes:
        room_id (int): The primary key of the room.
        room_name (str): The name of the room.
        default_rate (decimal): The default rate of the room.
    """

    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=255)
    default_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.room_name

    def get_final_rate(self, date):
        """
        Get the final rate for a specific date considering overridden rates and discounts.

        Args:
            date (datetime.date): The date for which to get the final rate.

        Returns:
            decimal: The final rate for the given date.
        """
        overridden_rate = OverriddenRoomRate.objects.filter(room_rate=self, stay_date=date).first()
        rate = overridden_rate.overridden_rate if overridden_rate else self.default_rate

        highest_discount = DiscountRoomRate.objects.filter(room_rate=self) \
                               .aggregate(Max('discount__discount_value'))['discount__discount_value__max'] or 0

        final_rate = rate - highest_discount if highest_discount else rate

        return final_rate


class OverriddenRoomRate(models.Model):
    """
    Model representing an overridden room rate for a specific date.

    Attributes:
        room_rate (RoomRate): The associated room rate.
        overridden_rate (decimal): The overridden rate for the room.
        stay_date (datetime.date): The date for which the overridden rate is applicable.
    """
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    overridden_rate = models.DecimalField(max_digits=10, decimal_places=2)
    stay_date = models.DateField()

    def __str__(self):
        return f"{self.room_rate.room_name} - {self.stay_date}"


class Discount(models.Model):
    """
    Model representing a discount.

    Attributes:
        discount_id (int): The primary key of the discount.
        discount_name (str): The name of the discount.
        discount_type (str): The type of the discount (fixed or percentage).
        discount_value (decimal): The value of the discount.
    """
    FIXED = 'fixed'
    PERCENTAGE = 'percentage'
    DISCOUNT_TYPE_CHOICES = [
        (FIXED, 'Fixed'),
        (PERCENTAGE, 'Percentage'),
    ]

    discount_id = models.IntegerField(primary_key=True)
    discount_name = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.discount_name


class DiscountRoomRate(models.Model):
    """
    Model representing the mapping between a room rate and a discount.

    Attributes:
        room_rate (RoomRate): The associated room rate.
        discount (Discount): The associated discount.
    """
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room_rate.room_name} - {self.discount.discount_name}"
