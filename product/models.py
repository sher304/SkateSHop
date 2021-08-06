from django.db import models

from users.models import CustomUser


class Category(models.Model):

    title = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title


class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии'),
        ('awaiting', 'ожидается')
    )

    name = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    likes = models.ManyToManyField(CustomUser, related_name='product')
    add_date = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='u_comments')
    body = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.product.name} - {self.name}'


class Checkout(models.Model):
    STATUS_CHOICES_REGION = (
        ('chuy', 'Chuy'),
        ('osh', 'Osh'),
        ('yssyk kul', 'Yssyk-Kul'),
        ('naryn', 'Naryn'),
        ('batken', 'Batken'),
        ('jalal abad', 'Jalal-Abad'),
        ('talas', 'Talas'),
    )

    STATUS_CHOICES_TYPE_ORDER = (
        ('self pickup', 'Self-pickup'),
        ('delivery', 'Delivery')
    )

    region = models.CharField(choices=STATUS_CHOICES_REGION, max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    number = models.BigIntegerField()
    address = models.CharField(max_length=100)
    postcode = models.IntegerField()
    type_order = models.CharField(choices=STATUS_CHOICES_TYPE_ORDER, max_length=50)
    add_time = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.surname} {self.name}'

