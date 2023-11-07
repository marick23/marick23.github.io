from django.db import models
import os
class Notice(models.Model):
    title = models.CharField(max_length=50)
    cont = models.TextField()

    head_image = models.ImageField(upload_to='notice/images/%Y/%m/%d', blank=True)
    file_upload = models.FileField(upload_to='notice/files/%Y/%m/%d/', blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]