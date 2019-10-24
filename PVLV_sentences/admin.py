from django.contrib import admin
from .models import (
    Sentence,
    Container,
    Collection,
    Author
)


admin.site.register(Sentence, Container, Collection, Author)
