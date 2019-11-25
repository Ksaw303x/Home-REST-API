from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    IntegerField,
    CharField,
    DateTimeField,
)
from PVLV_quotes.models import (
    Quote,
    Translation,
)


class TranslationSerializer(ModelSerializer):
    id = IntegerField(required=False)

    class Meta:
        model = Translation
        fields = [
            'id',
            'quote',
            'language_code',
            'title',
            'text',
        ]
        read_only_fields = ('quote',)


class QuoteSerializer(ModelSerializer):
    translations = TranslationSerializer(many=True)

    class Meta:
        model = Quote
        fields = [
            'id',
            'title',
            'status',
            'customizable',
            'text',
            'translations',
        ]

    def create(self, validated_data):
        translations = validated_data.pop('translations')
        print(validated_data)
        quote = Quote.objects.create(**validated_data)
        for translation in translations:
            Translation.objects.create(**translation, quote=quote)
        return quote

    def update(self, instance, validated_data):
        choices = validated_data.pop('choices')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        for choice in choices:
            if 'id' in choice.keys():
                if Translation.objects.filter(id=choice['id']).exists():
                    c = Translation.objects.get(id=choice['id'])
                    c.text = choice.get('text', c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Translation.objects.create(**choice, question=instance)
                keep_choices.append(c.id)

        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance
