from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at', ]
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(
        Category, models.CASCADE, related_name='category'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created_at', ]


class Sales(models.Model):
    product = models.OneToOneField(
        Product, models.CASCADE, related_name='sold'
    )
    amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
    amount_given = models.DecimalField(max_digits=7, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    quantity_bought = models.IntegerField()

    def __str__(self):
        return "model"

    class Meta:
        ordering = ['-paid_at']
        db_table = 'shop_sales'
        verbose_name = 'Sales'
        verbose_name_plural = 'Sales'
