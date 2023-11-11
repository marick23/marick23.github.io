from django.db import models

class OOTD(models.Model):

    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    head_image = models.ImageField(upload_to='OOTD/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/OOTD/{self.pk}/'