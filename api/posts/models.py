import uuid
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify

from .utils import get_read_time

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        self.tag = slugify(self.tag)
        return super(Tag, self).save(*args, **kwargs)

def post_images_directory_path(instance, filename):
    return '/'.join(['PostImages', str(uuid.uuid4().hex + ".png")])

def author_profile_images_directory_path(instance, filename):
    return '/'.join(['AuthorProfileImage', str(uuid.uuid4().hex + ".png")])

class Post(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    author = models.CharField(max_length=225)

    author_profile_image = models.ImageField(blank=True, null=True, width_field='width_field_author', height_field='height_field_author', upload_to=author_profile_images_directory_path)

    width_field_author = models.IntegerField(default=100)
    height_field_author = models.IntegerField(default=100)

    image_field = models.ImageField(blank=True, null=True, width_field='width_field', height_field='height_field', upload_to=post_images_directory_path)
    
    tags = models.ManyToManyField(Tag, blank=True)
    width_field = models.IntegerField(default=400)
    height_field = models.IntegerField(default=400)
    image_alt = models.CharField(max_length=225, blank=True)
    reading_time = models.CharField(max_length=225, blank=True)
    short_summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.author}'

    class Meta:
        ordering = ['-created_at', '-updated_at']

# Signals

def pre_save_slug_and_image_alt_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.image_alt = slugify(instance.title)
        instance.save()

pre_save.connect(pre_save_slug_and_image_alt_generator, sender=Post)

def pre_save_reading_time_generator(sender, instance, *args, **kwargs):
    if not instance.reading_time:
        generated_time = get_read_time(str(instance.content))
        instance.reading_time = f'{generated_time} min'
        instance.save()

pre_save.connect(pre_save_reading_time_generator, sender=Post)