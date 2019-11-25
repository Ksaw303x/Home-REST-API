from pavlov.settings import LANGUAGES

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


class ObjectTracking(models.Model):
    """
        To track the user that has created the entity
    """
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

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
    """
        List of tags of the
    """
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
    title = models.TextField(null=True, blank=False)  # optional if the tag is really important
    status = models.CharField(default='inactive', max_length=10)
    customizable = models.BooleanField(default=False)  # if the name of the subject can be changed with .format()
    text = models.TextField()
    tags = models.ManyToManyField(Tag)

    comments = GenericRelation(Comment, related_query_name="question")

    objects = QuestionManager()

    def __str__(self):
        return self.title

    @property
    def translations(self):
        return self.translation_set.all()


class Translation(ObjectTracking):
    """
        A QuoteTranslation is an exact copy of the Quote form but in another language,
        by default a quote is in English.
    """
    quote = models.ForeignKey(to=Quote, on_delete=models.CASCADE)
    language_code = models.TextField(default='italian', choices=LANGUAGES, unique=True)
    title = models.TextField(null=True, blank=False)  # optional if the tag is really important
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()


"""
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(QuoteTranslation, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comments = GenericRelation(Comment, related_query_name="answer")

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text
"""
