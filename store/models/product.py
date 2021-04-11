from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from store.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    old_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=1000, blank=True)

    class Meta:
        verbose_name_plural = 'Product'
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('store:detail', args=[self.id])

    def __str__(self):
        return self.title
