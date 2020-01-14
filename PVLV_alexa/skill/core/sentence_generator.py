from random import randrange


def welcome_sentence():
    sentence_list = [
        'Ciao Biondo, dimmi pure che ti serve.',
        'Buona li, dimmi tutto.',
    ]
    idx = randrange(0, len(sentence_list)-1)
    return sentence_list[idx]


def waiting_sentence():
    sentence_list = [
        'Che vuoi fare adesso?',
        'Allora? Dobbiamo starcene qui in silenzio ancora per quanto?',
        'Tranquillo, pensa con calma, abbiamo tuuutto il giorno.'
    ]
    idx = randrange(0, len(sentence_list)-1)
    return sentence_list[idx]
