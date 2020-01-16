import logging
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import (
    is_request_type,
)

from .music import playback_control
from PVLV_alexa.skill.pavlov_skill.data import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class PlayMusicHandler(AbstractRequestHandler):
    """
    Launch radio for skill launch or PlayAudio intent.
    """
    def can_handle(self, handler_input):
        return is_request_type("PlayMusic")(handler_input)

    def handle(self, handler_input):
        logger.info("In LaunchRequestHandler")

        playback_info = playback_control.get_playback_info(handler_input)

        if not playback_info.get('has_previous_playback_session'):
            message = WELCOME_MSG
            reprompt = WELCOME_REPROMPT_MSG
        else:
            playback_info['in_playback_session'] = False
            message = WELCOME_PLAYBACK_MSG.format(
                AUDIO_DATA[
                    playback_info.get("play_order")[
                        playback_info.get("index")]].get("title"))
            reprompt = WELCOME_PLAYBACK_REPROMPT_MSG

        return handler_input.response_builder.speak(message).ask(
            reprompt).response
