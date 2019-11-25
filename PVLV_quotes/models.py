from pavlov.settings import LANGUAGES

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


class Container(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class ObjectTracking(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class Comment(models.Model):
    text = models.TextField(null=False, blank=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.text[:20]


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="active")

    def all_objects(self):
        return super().get_queryset()

    def inactive(self):
        return self.all_objects().filter(status='inactive')


class Tag(ObjectTracking):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = []


class Quote(ObjectTracking):
    """
    Its a sentence, a joke, a quote that should be stored on the DB,
    This is the main entity and all is built around this
    """
    # container = models.ForeignKey(to=Container, on_delete=models.CASCADE)
    # meta = models.ForeignKey(to=Meta, on_delete=models.CASCADE)
    customizable = models.BooleanField(default=False)  # if the name of the subject can be changed with .format()
    text = models.TextField()
    author = models.TextField
    tags = models.TextField()

    def __str__(self):
        return self.text


class QuoteTranslation(models.Model):
    """
    A QuoteTranslation is an exact copy of the Quote form but in another language,
    by default a quote is in English.
    """
    quote = models.ForeignKey(to=Quote, on_delete=models.CASCADE)
    language_code = models.TextField(default='italian', choices=LANGUAGES, unique=True)
    text = models.TextField(default='A translated quote')
