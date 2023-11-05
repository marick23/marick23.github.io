from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=50)
    cont = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'
