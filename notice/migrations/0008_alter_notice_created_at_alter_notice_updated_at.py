# Generated by Django 4.2.5 on 2023-11-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_notice_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
