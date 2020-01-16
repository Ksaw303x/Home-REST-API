import logging
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import (
    is_request_type,
    is_intent_name,
    get_intent_name
)

from PVLV_alexa.skill.pavlov_skill.data import *


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """
    Handler for skill launch.
    """
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        return (
            handler_input.response_builder
            .speak(welcome_msg())
            .ask(waiting_msg())
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """
    Handler for Help Intent.
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        return (
            handler_input.response_builder
            .speak(HELP_MSG)
            .ask(waiting_msg())
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """
    Single handler for Cancel and Stop Intent.
    """
    def can_handle(self, handler_input):
        cancel = is_intent_name("AMAZON.CancelIntent")(handler_input)
        stop = is_intent_name("AMAZON.StopIntent")(handler_input)
        return cancel or stop

    def handle(self, handler_input):
        return (
            handler_input.response_builder
            .speak(STOP_MSG)
            .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """
    Handler for Session End.
    """
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # Any cleanup logic goes here.
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """
    The intent reflector is used for interaction model testing and debugging.
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
            .ask(waiting_msg())
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """
    Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)

        return (
            handler_input.response_builder
            .speak(EXCEPTION_MSG)
            .ask(waiting_msg())
            .response
        )
