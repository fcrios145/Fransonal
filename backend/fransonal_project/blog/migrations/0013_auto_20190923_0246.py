# Generated by Django 2.2.5 on 2019-09-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_short_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
