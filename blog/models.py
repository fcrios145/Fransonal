from django.db import models
from django.template.defaultfilters import slugify
import markdown


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(null=True)

    def get_rendered(self):
        return markdown.markdown(self.description, extensions=['fenced_code','codehilite', 'tables'])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
