from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import (is_request_type, is_intent_name, get_intent_name)

from PVLV_alexa.skill.core.sentence_generator import welcome_sentence
from PVLV_alexa.skill.core.sentence_generator import waiting_sentence

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

psb = SkillBuilder()


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        return (
            handler_input.response_builder
            .speak(welcome_sentence())
            .ask(waiting_sentence())
            .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        return is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Buongiorno Mondo"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(waiting_sentence())
            .response
        )


class HowAreYouIntentHandler(AbstractRequestHandler):
    """How are you."""
    def can_handle(self, handler_input):
        return is_intent_name("HowAreYouIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Mah, io benone, tu? Anzi no non mi iteressa"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(waiting_sentence())
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Mmmh leggi le istruzioni"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(waiting_sentence())
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        cancel = is_intent_name("AMAZON.CancelIntent")(handler_input)
        stop = is_intent_name("AMAZON.StopIntent")(handler_input)
        return cancel or stop

    def handle(self, handler_input):
        speak_output = "Se vedemo!"

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # Any cleanup logic goes here.
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        intent_name = get_intent_name(handler_input)
        speak_output = "Hai appena triggerato " + intent_name + "."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(waiting_sentence())
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)

        speak_output = "Non ti capisco, parla più forte."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


# Registration of all handlers
psb.add_request_handler(LaunchRequestHandler())


skill = psb.create()
