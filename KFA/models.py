from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
class KFA(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    cont = MarkdownxField()
    name = models.CharField(max_length=100, default=0.0)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    option_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    head_image = models.ImageField(upload_to='KFA/images/상품이미지/', blank=True)
    detail_image1 = models.ImageField(upload_to='KFA/images/상품상세이미지/', blank=True)
    detail_image2 = models.ImageField(upload_to='KFA/images/상품상세이미지/', blank=True)
    size_image = models.ImageField(upload_to='KFA/images/상품상세이미지/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/KFA/{self.pk}/'

    def __str__(self):
        return self.title

    def get_content_markdown(self):
        return markdown(self.content)