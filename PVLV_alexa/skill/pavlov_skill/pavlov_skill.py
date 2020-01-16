from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler

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

from PVLV_alexa.skill.pavlov_skill.core.music_intents.default_player_intents import (
    StartPlaybackHandler,
    PausePlaybackHandler,
)

from PVLV_alexa.skill.pavlov_skill.core.music_intents.play import (
    PlayMusicHandler
)


class CheckAudioInterfaceHandler(AbstractRequestHandler):
    """
    Check if device supports audio play.
    This can be used as the first handler to be checked, before invoking
    other handlers, thus making the skill respond to unsupported devices
    without doing much processing.
    """
    def can_handle(self, handler_input):
        if handler_input.request_envelope.context.system.device:
            # Since skill events won't have device information
            return handler_input.request_envelope.context.system.device.supported_interfaces.audio_player is None
        else:
            return False

    def handle(self, handler_input):
        handler_input.response_builder.speak().set_should_end_session(True)
        return handler_input.response_builder.response


sb = SkillBuilder()

# Launch
sb.add_request_handler(CheckAudioInterfaceHandler())
sb.add_request_handler(LaunchRequestHandler())

# Greetings
sb.add_request_handler(HowAreYouIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())

# Music
sb.add_request_handler(PlayMusicHandler())
sb.add_request_handler(StartPlaybackHandler())
sb.add_request_handler(PausePlaybackHandler())

# Default intents
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(IntentReflectorHandler())
sb.add_exception_handler(CatchAllExceptionHandler())


skill = sb.create()
