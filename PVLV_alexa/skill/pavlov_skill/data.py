from random import randrange


WELCOME_MSG = "Welcome to the Alexa Dev Chat Podcast. You can say, play the audio to begin the podcast."
WELCOME_REPROMPT_MSG = "You can say, play the audio, to begin."
WELCOME_PLAYBACK_MSG = "You were listening to {}. Would you like to resume?"
WELCOME_PLAYBACK_REPROMPT_MSG = "You can say yes to resume or no to play from the top"
DEVICE_NOT_SUPPORTED = "Sorry, this skill is not supported on this device"
LOOP_ON_MSG = "Loop turned on."
LOOP_OFF_MSG = "Loop turned off."
HELP_MSG = "Per usare questa skill"
HELP_PLAYBACK_MSG = WELCOME_PLAYBACK_MSG
HELP_DURING_PLAY_MSG = "You are listening to the Alexa Dev Chat Podcast. You can say, Next or Previous to navigate through the playlist. At any time, you can say Pause to pause the audio and Resume to resume."
STOP_MSG = "Ci vediamo."
EXCEPTION_MSG = "Questo non è un comando. Usa, help, per capire cosa puoi fare."
PLAYBACK_PLAY = "This is {}"
PLAYBACK_PLAY_CARD = "Playing {}"
PLAYBACK_NEXT_END = "You have reached the end of the playlist"
PLAYBACK_PREVIOUS_END = "You have reached the start of the playlist"

HOW_ARE_YOU_MSG_1 = "Mah, io benone, tu? Anzi no non mi iteressa"
HOW_ARE_YOU_MSG_2 = "Per ora tutto apposto, grazie"
HOW_ARE_YOU_MSG_3 = "Fantasticamente, sono alle versione 3 adesso"

DYNAMODB_TABLE_NAME = "Audio-Player-Multi-Stream"

AUDIO_DATA = [
    {
        "title": "Episode 22",
        "url": "https://feeds.soundcloud.com/stream/459953355-user-652822799-episode-022-getting-started-with-alexa-for-business.mp3",
    },
    {
        "title": "Episode 23",
        "url": "https://feeds.soundcloud.com/stream/476469807-user-652822799-episode-023-voicefirst-in-2018-where-are-we-now.mp3",
    },
    {
        "title": "Episode 24",
        "url": "https://feeds.soundcloud.com/stream/496340574-user-652822799-episode-024-the-voice-generation-will-include-all-generations.mp3",
    }
]


def welcome_msg():
    sentence_list = [
        'Ciao Biondo, dimmi pure che ti serve.',
        'Buona li, dimmi tutto.',
        'Ciao Amore, cosa ti serve?',
        'Sono caldo, illuminami con le tue richieste.',
        'Eccomi qui, per ascoltare le tue cagate, dimmi.',
    ]
    idx = randrange(0, len(sentence_list)-1)
    return sentence_list[idx]


def waiting_msg():
    sentence_list = [
        'Che vuoi fare adesso?',
        'Allora? Dobbiamo starcene qui in silenzio ancora per quanto?',
        'Tranquillo, pensa con calma, abbiamo tuuutto il giorno.'
    ]
    idx = randrange(0, len(sentence_list)-1)
    return sentence_list[idx]
