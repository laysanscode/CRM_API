from django.db import models
from Users.models import Users_data

class Category(models.Model):
    Category_name = models.CharField(max_length=1000)
    Category_img = models.ImageField(upload_to="media/Category/")  # ✅ fixed path
    created_at = models.DateTimeField(auto_now_add=True)     # ✅ fixed timestamp
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Category_name


class Products(models.Model):
    Dealer = models.ForeignKey(Users_data, on_delete=models.CASCADE)
    Products_name = models.CharField(max_length=1000)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Products_img = models.ImageField(upload_to="media/Products/")  # ✅ fixed path
    Quality = models.BigIntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total_Price = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)     # ✅ fixed timestamp
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Products_name
