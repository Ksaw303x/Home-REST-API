import logging
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import Response

from PVLV_alexa.skill.pavlov_skill.core.util.sentence_generator import waiting_sentence


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
        speech = "Mah, io benone, tu? Anzi no non mi iteressa"
        speech = "Per ora tutto apposto, grazie"
        speech = "Fantasticamente, sono alle versione 3 adesso"

        return (
            handler_input.response_builder
            .speak(speech)
            .ask(waiting_sentence())
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
            .ask(waiting_sentence())
            .response
        )