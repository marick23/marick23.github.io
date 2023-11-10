from django.db import models

class KFA(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    cont = models.TextField()
    name = models.CharField(max_length=100, default=0.0)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    option_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    head_image = models.ImageField(upload_to='KFA/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/KFA/{self.pk}/'

    def __str__(self):
        return self.title