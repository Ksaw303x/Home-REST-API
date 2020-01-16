import logging
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import (
    is_intent_name,
)

from .music import playback_control

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class PausePlaybackHandler(AbstractRequestHandler):
    """
    Handler for stopping audio.
    Handles Stop, Cancel and Pause Intents and PauseCommandIssued event.
    """
    def can_handle(self, handler_input):
        playback_info = playback_control.get_playback_info(handler_input)

        return (playback_info.get("in_playback_session")
                and (
                    is_intent_name("AMAZON.StopIntent")(handler_input)
                    or is_intent_name("AMAZON.CancelIntent")(handler_input)
                    or is_intent_name("AMAZON.PauseIntent")(handler_input))
                )

    def handle(self, handler_input):
        logger.info("PausePlaybackHandler")
        return playback_control.Controller.stop(handler_input)


class StartPlaybackHandler(AbstractRequestHandler):
    """
    Handler for Playing audio on different events.
    Handles PlayAudio Intent, Resume Intent.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.ResumeIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In StartPlaybackHandler")
        return playback_control.Controller.play(handler_input)
