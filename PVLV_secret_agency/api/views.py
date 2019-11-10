from PVLV_secret_agency.models import Target
from PVLV_secret_agency.api.serializers import TargetSerializer

from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.viewsets import ModelViewSet


class TargetSnippetViewSet(ModelViewSet):

    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = (IsAuthenticated,)
