from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/KLEAGUE/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'


class KLEAGUE(models.Model):
    objects = None
    league_name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)
    cont = MarkdownxField()
    name = models.CharField(max_length=100, default=0.0)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    option_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    head_image = models.ImageField(upload_to='KLEAGUE/images/상품이미지/', blank=True)
    detail_image1 = models.ImageField(upload_to='KLEAGUE/images/상품상세이미지/', blank=True)
    detail_image2 = models.ImageField(upload_to='KLEAGUE/images/상품상세이미지/', blank=True)
    size_image = models.ImageField(upload_to='KLEAGUE/images/상품상세이미지/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/KLEAGUE/{self.pk}/'

    def __str__(self):
        return self.title

    def get_content_markdown(self):
        return markdown(self.content)