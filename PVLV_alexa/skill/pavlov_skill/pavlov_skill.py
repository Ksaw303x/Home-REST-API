from ask_sdk_core.skill_builder import SkillBuilder

from PVLV_alexa.skill.pavlov_skill.core.base_intents.base_intents import (
    LaunchRequestHandler,
    HelpIntentHandler,
    SessionEndedRequestHandler,
    CancelOrStopIntentHandler,
    IntentReflectorHandler,
    CatchAllExceptionHandler
)

from PVLV_alexa.skill.pavlov_skill.core.greetings_intents.greetings import (
    HowAreYouIntentHandler,
    HelloWorldIntentHandler,
)

sb = SkillBuilder()


# Greetings
sb.add_request_handler(HowAreYouIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())

# Default intents
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(IntentReflectorHandler())
sb.add_exception_handler(CatchAllExceptionHandler())


skill = sb.create()
