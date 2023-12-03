# Generated by Django 4.2.5 on 2023-12-03 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ask', '0003_ask_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', markdownx.models.MarkdownxField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask.ask')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
