from django.db import models

# Create your models here.
class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    review_title = models.CharField(max_length=128)
    review_content = models.CharField(max_length=3000)
    review_url = models.CharField(max_length=255)
    found_helpful = models.IntegerField(default=0)
    verified_purchase = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255)
