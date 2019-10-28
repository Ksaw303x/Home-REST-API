from PVLV_quotes.models import (
    Quote,
    QuoteTranslation
)
from PVLV_quotes.api.serializers import (
    QuoteSerializer,
    QuoteTranslationSerializer,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from rest_framework.viewsets import ModelViewSet


class QuotesSnippetViewSet(ModelViewSet):

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['get'])
    def translations(self, request, pk=None):
        quote = self.get_object()
        translations = QuoteTranslation.objects.filter(quote=quote)
        for translation in translations:
            print(translation)
        if translations:
            serialized_data = QuoteTranslationSerializer(translations, many=True)
        else:
            serialized_data = []
        return Response(serialized_data, HTTP_200_OK)


"""
    @action(detail=True, methods=['post'])
    def translation(self, request, pk=None):
        quote = self.get_object()
        data = request.data
        # data['translation'] = quote.pk
        serialized_data = QuoteTranslationSerializer(data=request.data)
        if serialized_data.is_valid():
            return Response(serialized_data, HTTP_200_OK)
        return Response(serialized_data, HTTP_400_BAD_REQUEST)

"""