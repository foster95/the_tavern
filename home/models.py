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
        return (
            f"Featured Product for {month_label} {self.year}: {self.product}"
            )


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

class ContactForm(models.Model):
    TOPIC_ORDER = "order"
    TOPIC_MATERIALS = "materials"
    TOPIC_RETURNS = "returns"
    TOPIC_TECHICNAL = "technical"
    TOPIC_OTHER = "other"

    TOPIC_CHOICES = [
        (TOPIC_ORDER, "I have a question about my order"),
        (TOPIC_MATERIALS, "A question about materials or dice care"),
        (TOPIC_RETURNS, "My loot arrived damaged/faulty"),
        (TOPIC_TECHICNAL, "Report a glitch in the weave"),
        (TOPIC_OTHER, "General feedback or tavern tales"),
    ]

    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)

    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.get_topic_display() or 'No topic'}"
