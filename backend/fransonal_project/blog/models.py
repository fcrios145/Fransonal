from django.db import models


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



