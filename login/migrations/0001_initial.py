# Generated by Django 4.2.7 on 2023-11-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('memberid', models.TextField()),
                ('pw', models.TextField()),
                ('phonenumber', models.TextField()),
                ('email', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
