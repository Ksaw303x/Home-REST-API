from django.contrib import admin
from .models import (
    Quote,
    QuoteTranslation
)


admin.site.register([Quote, QuoteTranslation])
