from django.db import models
from django.db.models.signals import pre_save
import markdown


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(models.Model):
    name = models.CharField(max_length=100)


class Article(TimestampedModel):
    name = models.TextField(max_length=100, null=False)
    hero_image = models.ImageField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    raw_content = models.TextField(default='')
    compiled_content = models.TextField(default='')


def pre_save_article(sender, instance, **kwargs):
    # instance.compiled_content = instance.name
    instance.compiled_content = markdown.markdown(instance.raw_content, extensions=['fenced_code', 'codehilite', 'tables'])


pre_save.connect(pre_save_article, sender=Article)