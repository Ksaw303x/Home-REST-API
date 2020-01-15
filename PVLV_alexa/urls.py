from django.urls import path
from PVLV_alexa.skill.pavlov_skill.pavlov_skill import skill
from django_ask_sdk.skill_adapter import SkillAdapter

from PVLV_alexa.views import alexa_home

my_skill_view = SkillAdapter.as_view(skill=skill)

urlpatterns = [
    path('', alexa_home),
    path('pavlov/', my_skill_view, name='index'),
]
