# Generated by Django 4.2.5 on 2023-11-23 23:09

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0008_alter_notice_created_at_alter_notice_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
