from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else self.body if self.body else self.email if self.email else str(self.date)

    def snippet(self):
        return self.body if len(self.body) < 20 else self.body[:10] + " • • •"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super(Contact, self).save(*args, **kwargs)
