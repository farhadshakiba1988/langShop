from django.db import models
from django.urls import reverse


class Youtube(models.Model):
    name = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    image = models.ImageField(upload_to='image/', blank=True)
    des = models.CharField(max_length=400, blank=True)
    created = models.DateTimeField(auto_now=True, blank=True)
    see = models.SmallIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Youtube'
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('store:detail', args=[self.id])

    def __str__(self):
        return self.title
