from django.db import models

# Create your models here.

class ProductOfTheMonth(models.Model):
    """ Model for featured product of the month """

    product = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE, related_name='featured_in_month'
    )
    month = models.DateField(unique=True)

    def __str__(self):
        return f"Featured Product for {self.month.strftime('%B %Y')}: {self.product}"
