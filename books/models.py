from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    title= models.CharField(max_length=200)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=6)
    pages = models.IntegerField(default=4)
    isbn = models.CharField(max_length=50)
    cover_photo = models.ImageField(upload_to='uploads/%Y/%m/%d')

    #date fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
