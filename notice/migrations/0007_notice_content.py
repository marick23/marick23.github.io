# Generated by Django 4.2.5 on 2023-11-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_remove_notice_cont'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
