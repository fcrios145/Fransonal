# Generated by Django 2.2.5 on 2019-09-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_article_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='compiled_content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='raw_content',
            field=models.TextField(default=''),
        ),
    ]