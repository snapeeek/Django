from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('shop_name', )

    def __str__(self):
        return self.shop_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField(default=0)

    class Meta:
        ordering = ('product_name', )

    def __str__(self):
        return self.product_name


class ShoppingPosition(models.Model):
    product_count = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="Product+")
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)

    def countPrice(self):
        return self.product.product_price * self.product_count

    def __str__(self):
        return self.product.__str__() + " x" + self.product_count.__str__() + " " + self.shop.__str__()
