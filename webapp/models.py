from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Category title')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Category description')

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Product title')
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name='Product description'
    )
    category = models.ForeignKey(
        to='webapp.Category',
        verbose_name='Category',
        null=False,
        blank=False,
        related_name='products',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created time')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='product price')
    image = models.ImageField(upload_to='static/images', blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.created_at} {self.description}"

    @property
    def my_image(self):
        if self.image:
            return self.image.url
        return ''
