import calendar
from django.db import models

MONTH_CHOICES = [(i, calendar.month_name[i]) for i in range(1, 13)]

class ProductOfTheMonth(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("year", "month")
        ordering = ["-year", "-month"]

    def __str__(self):
        try:
            month_int = int(self.month)
            month_label = calendar.month_name[month_int]
        except (TypeError, ValueError, IndexError):
            month_label = str(self.month)
        return f"Featured Product for {month_label} {self.year}: {self.product}"
