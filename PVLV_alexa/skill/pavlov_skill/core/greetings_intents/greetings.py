import logging
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import Response

from PVLV_alexa.skill.pavlov_skill.data import *


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class HowAreYouIntentHandler(AbstractRequestHandler):
    """
    How are you intent
    For a simply funny sentence without a response
    """
    def can_handle(self, handler_input):
        return is_intent_name("HowAreYouIntent")(handler_input)

    def handle(self, handler_input):
        return (
            handler_input.response_builder
            .speak(HOW_ARE_YOU_MSG_3)
            .ask(waiting_msg())
            .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        return is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        speech = "Ciao Terra"

        return (
            handler_input.response_builder
            .speak(speech)
            .ask(waiting_msg())
            .response
        )
