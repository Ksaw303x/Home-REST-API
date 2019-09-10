from Crypto.Cipher import AES, CAST
from django.conf import settings
from django.utils import timezone

from DataWeb.licence import LicenceManager


def fill_to_8(text):
    q, r = divmod(len(text), 8)
    if r:
        q += 1
    if isinstance(text, bytes):
        res = text.rjust(q*8, b'0')
    else:
        res = text.rjust(q*8, '0')
    return res


class Crypto:

    def get_default_passhphrase(self):
        licence = LicenceManager.load_licence()

        d_k = licence.company_default_devices_crypto_key()

        if d_k:
            return d_k

        #Default KEY
        return '2b7e151628aed2a6'

    def __init__(self, msg='', cast5_type=False, key=None):
        self.msg = msg
        self.cast5 = cast5_type
        if key:
            if not isinstance(key, bytes):
                self.key = key.encode()
            else:
                self.key = key
        else:
            self.key = self.get_default_passhphrase().encode()

    def __call__(self, *args, **kwargs):
        if self.cast5:
            cipher = CAST.new(self.key, CAST.MODE_ECB)
            if not isinstance(self.msg, bytes):
                self.msg = self.msg.encode()
        else:
            cipher = AES.new(self.key, AES.MODE_ECB)
        try:
            dec = cipher.decrypt(self.msg)
            #print("{} decodificato: <{}>".format("CAST" if self.cast5 else "AES", dec))
        except ValueError as exc:
            """
            now = timezone.localtime(timezone.now(), timezone.get_current_timezone())
            print("{} - Errore in decodifica {}.\n{}".format("CAST" if self.cast5 else "AES", now.strftime('%Y-%m-%d %H:%M:%S'), exc))
            if self.cast5:
                print(self.msg)
                print(len(self.msg))
            """
            dec = None
        return dec

    @classmethod
    def encrypt(cls, myMessage, cast5=False, key=None):

        if key:
            if not isinstance(key, bytes):
                k = key.encode()
            else:
                k = key
        else:
            k = cls.get_default_passhphrase().encode()

        if cast5:
            cipher = CAST.new(k, CAST.MODE_ECB)
            myMessage = fill_to_8(myMessage)
        else:
            cipher = AES.new(k, AES.MODE_ECB)
        if not isinstance(myMessage, bytes):
            myMessage = myMessage.encode()
        _encrypted = cipher.encrypt(myMessage)
        return _encrypted

    def __str__(self):
        return "Cifrario `{}`, chiave <{}>".format("CAST" if self.cast5 else "AES", self.get_default_passhphrase())
