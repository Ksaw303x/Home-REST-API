from rest_framework.serializers import ModelSerializer
from PVLV_quotes.models import (
    Quote,
    QuoteTranslation
)


class QuoteTranslationSerializer(ModelSerializer):

    class Meta:
        model = QuoteTranslation
        fields = (
            'quote',
            'language_code',
            'text',
        )
        read_only_field = ('quote',)


class QuoteSerializer(ModelSerializer):
    # translations = QuoteTranslationSerializer(many=True)

    class Meta:
        model = Quote
        fields = (
            'id',
            'customizable',
            'text',
            'tags',
            # 'translations',
        )
