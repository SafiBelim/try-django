from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

from .utils import slugify_instance_title
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120) 
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False,auto_now=False, null=True, blank=True)

    #Override the save method to generate the slug title
    def save(self, *args, **kwargs):
        # if self.slug is None:
            # self.slug = slugify(self.title)
        super().save(*args, **kwargs)




#django signals example
def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)
        

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Article)
    
