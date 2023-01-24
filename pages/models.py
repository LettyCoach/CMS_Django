# from translations.models import Translatable
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from news.models import New


class Page(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    languageChoices = (
        ('en', 'English'),
        ('de', 'Germen'),
        ('fr', 'French')
    )
    lang = models.CharField(
        max_length=2,
        choices=languageChoices,
        default='en'
    )
    body = models.TextField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE,
                            related_name='nComments', blank=True, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE,
                             related_name='pComments', blank=True, null=True)
