from django.db import models
from django.utils import timezone
from pavlov.settings import LANGUAGES


class Container(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Meta(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)


class Quote(models.Model):
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
