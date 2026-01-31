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
        verbose_name = "Product of the Month"
        verbose_name_plural = "Product of the Month"

    def __str__(self):
        try:
            month_int = int(self.month)
            month_label = calendar.month_name[month_int]
        except (TypeError, ValueError, IndexError):
            month_label = str(self.month)
        return f"Featured Product for {month_label} {self.year}: {self.product}"

class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=80)
    tagline = models.CharField(max_length=120, blank=True) 
    sort_order = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return f"{self.name} — {self.quote[:40]}..."