# Generated by Django 4.2.6 on 2023-11-30 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KLEAGUE', '0010_alter_category_options_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='KLEAGUE.kleague'),
        ),
    ]
