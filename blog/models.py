from django.db import models
from django.template.defaultfilters import slugify
import markdown


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(null=True)
    short_summary = models.TextField()
    public = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.title

    def get_rendered_body(self):
        return markdown.markdown(self.description, extensions=['fenced_code','codehilite', 'tables'])

    def get_rendered_short_description(self):
        return markdown.markdown(self.short_summary)

    def get_publics():
        return Post.objects.filter(public=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
