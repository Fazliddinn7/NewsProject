# import pillow
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,
                            null=True,
                            blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            null=True,
                            blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Categories,
                                 on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email
