from django.urls import path
from PVLV_alexa.skill.pavlov_skill import skill
from django_ask_sdk.skill_adapter import SkillAdapter

pavlov_skill_view = SkillAdapter.as_view(
    skill=skill)

urlpatterns = [
    path('', pavlov_skill_view, name='index'),
]