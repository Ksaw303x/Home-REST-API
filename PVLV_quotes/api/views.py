from PVLV_quotes.models import (
    Quote,
    Translation
)
from PVLV_quotes.models import *
from PVLV_quotes.api.serializers import (
    QuoteSerializer,
    TranslationSerializer,
)
from PVLV_quotes.api.serializers import *
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
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters

"""
class PollFilter(FilterSet):
    tags = filters.CharFilter(method="filter_by_tags")

    class Meta:
        model = Question
        fields = ["tags"]

    def filter_by_tags(self, queryset, name, value):
        tag_names = value.strip().split(",")
        tags = Tag.objects.filter(name__in=tag_names)
        return queryset.filter(tags__in=tags).distinct()
"""


class PollViewSet(ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend,)
    # filter_class = PollFilter

    @action(detail=True, methods=["GET"])
    def translations(self, request, id=None):
        question = self.get_object()
        choices = Translation.objects.filter(question=question)
        serializer = TranslationSerializer(choices, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def choice(self, request, id=None):
        question = self.get_object()
        data = request.data
        data["question"] = question.id
        serializer = TranslationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)
