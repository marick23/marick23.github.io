# Generated by Django 4.2.5 on 2023-11-12 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]