from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

class OOTD(models.Model):

    title = models.CharField(max_length=200, verbose_name='제목')
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='OOTD/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/OOTD/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.content)