from PVLV_secret_agency.models import (
    Target,
    Guild,
    TargetMonitoringPlatform,
    TargetPersonalData,
)
from rest_framework.serializers import ModelSerializer


class GuildSerializer(ModelSerializer):

    class Meta:
        model = Guild
        fields = (
            'platform',
            'guild_id',
            'channel_id',
        )


class TargetSerializer(ModelSerializer):

    sending_points = GuildSerializer(many=True)

    class Meta:
        model = Target
        fields = (
            'id',
            'owner',
            'monitorable',
            'sending_points',
            'name',
            'age',
        )
