from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import  slugify
from django.urls import reverse
import markdown


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.name

class Article(TimestampedModel):
    name = models.CharField(max_length=100, null=False, unique=True)
    hero_image = models.ImageField(upload_to='images/', null=False, blank=True, default='images/default.jpg')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    raw_content = models.TextField(default='')
    compiled_content = models.TextField(default='')
    tags = models.ManyToManyField(Tag)
    short_content = models.TextField(max_length=150, default='')
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse('articulo', kwargs={
            'slug': self.slug
        })

    def get_update_url(self):
        return reverse('editar_articulo', kwargs={
            'slug': self.slug
        })

    # def get_delete_url(self):
    #     return reverse('post-delete', kwargs={
    #         'pk': self.pk
    #     })


def pre_save_article(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    instance.compiled_content = markdown.markdown(instance.raw_content, extensions=['fenced_code', 'codehilite', 'tables'])


pre_save.connect(pre_save_article, sender=Article)