from django.contrib import admin
from .models import (
    Quote,
    Translation
)
from .models import *


admin.site.register([
    Quote,
    Translation,
    Comment,
    Tag,
    # Answer,
])
