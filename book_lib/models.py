from django.db import models
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=False)
    publish_date = models.DateField()
    isbn = models.CharField(max_length=13 , null=False ) 
    image = models.ImageField(upload_to='images/%y/%m/%d',null=True,blank=True)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
