# Generated by Django 4.2.6 on 2023-11-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OOTD', '0004_rename_cont_ootd_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ootd',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='ootd',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='OOTD/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='ootd',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='ootd',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='작성일'),
        ),
        migrations.AlterField(
            model_name='ootd',
            name='title',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
    ]
