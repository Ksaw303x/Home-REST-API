from django.contrib import admin
from PVLV_secret_agency.models import (
    Target,
    Guild,
    TargetMonitoringPlatform,
    TargetPersonalData,
)

admin.site.register([Target, Guild, TargetMonitoringPlatform, TargetPersonalData])
