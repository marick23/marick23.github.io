from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os
class Notice(models.Model):
    title = models.CharField(max_length=50)
    content = MarkdownxField()
    head_image = models.ImageField(upload_to='notice/images/%Y/%m/%d', blank=True)
    file_upload = models.FileField(upload_to='notice/files/%Y/%m/%d/', blank=True)

    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)