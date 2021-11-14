from django.db import models

# Create your models here.
class Review(models.Model):
    #review_id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=3000)
    url = models.CharField(max_length=255)
    found_helpful = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    product = models.CharField(max_length=255)
    rating = models.IntegerField(default=1)
