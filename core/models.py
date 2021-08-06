from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=40)
    message = models.TextField()

    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
