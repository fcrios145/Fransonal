# Generated by Django 2.2.5 on 2019-09-22 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190922_0509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='published',
        ),
    ]
