# Generated by Django 2.2.5 on 2019-09-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190923_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='short_content',
            field=models.TextField(default='', max_length=150),
        ),
    ]