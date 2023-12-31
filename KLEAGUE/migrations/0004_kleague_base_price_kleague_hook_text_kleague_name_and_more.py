# Generated by Django 4.2.6 on 2023-11-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KLEAGUE', '0003_kleague_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='kleague',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='kleague',
            name='hook_text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='kleague',
            name='name',
            field=models.CharField(default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='kleague',
            name='option_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
