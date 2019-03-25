from django.db import models
from django.template.defaultfilters import slugify
import markdown
import os


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(null=True)
    short_summary = models.TextField()

    def __str__(self):
        return self.title

    def get_rendered_body(self):
        return markdown.markdown(self.description, extensions=['fenced_code','codehilite', 'tables'])

    def get_rendered_short_description(self):
        return markdown.markdown(self.short_summary)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

# Create your models here.
class Post2(models.Model):
    managed = False

    def __str__(self):
        return self.title

    def get_rendered_body(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        print(script_dir)
        rel_path = "posts/como_instalar_virtualenv.md"
        abs_file_path = os.path.join(script_dir, rel_path)
        file = open(abs_file_path, 'r').read()
        return markdown.markdown(file, extensions=['fenced_code','codehilite', 'tables'])