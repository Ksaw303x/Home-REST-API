import json
import logging
import string
import random

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from basic.utils import (binary_to_b64_str, b64string_to_binary)
from devices.crypto import Crypto

logger = logging.getLogger(__name__)


class TDBaseServerAPI(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    PING = 0
    STAMPING = 1

    # incoming messages types
    PING_PREFIX = 'P'

    # replies
    REBOOT_REPLY = 'REB'
    ERROR_REPLY = 'ERR'
    OK_REPLY = 'NON'
    SETTINGS_REPLY = 'SET'
    NETWORK_REPLY = 'NET'
    REL_REPLY = 'REL'

    def __init__(self):
        super(TDBaseServerAPI, self).__init__()

        self.buffer_len_in = 128
        self.buffer_len_out = 192

    def _generate_fill_data(self, actual_string):
        """
        Affianca alla actual string caratteri random per rendere la crittografia più random nelle reply corte
        :param actual_string: striga attuale
        :return: la stringa con i caratteri random affiancati.
        """
        missing = self.buffer_len_out - len(actual_string) - 1  # cause of /0
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(missing))

    def _build_reply(self, reply_type):
        """
        Costruisce la risposta da inviare al terminale.
        :param reply_type: Una delle reply definite globalmente ed accettate dal terminale.
        :return: Un HttpResponse contenente come body ciò definito nel risposta richiesta.
        """

        def reb():
            """
            REPLY REB to reboot the device
            """
            _content_in_clear = '{};'.format(self.REBOOT_REPLY)
            _status_code = status.HTTP_200_OK
            return _content_in_clear, _status_code

        def err():
            """
            REPLY ERR when there is nothing to do:
            """
            _content_in_clear = '{};'.format(self.ERROR_REPLY)
            _status_code = status.HTTP_400_BAD_REQUEST
            return _content_in_clear, _status_code

        def non():
            """
            REPLY NON when there is nothing to do:
            """
            _content_in_clear = '{};'.format(self.OK_REPLY)
            _status_code = status.HTTP_200_OK
            return _content_in_clear, _status_code

        def rel():
            """
            REPLY REL open a relè on TDBase:
            N.B.: i due relè vengono identificati come 0 e 1 ed il tempo viene dato in secondi, il tempo viene salvato in un uint16_t,
            Relè e tempo vanno messi in un unica stringa separati da uno spazio. Il tempo è espresso in secondi.
            """
            _content_in_clear = '{};{};'.format(
                self.REL_REPLY,
                '1, 20',
            )
            _status_code = status.HTTP_200_OK
            return _content_in_clear, _status_code

        def set():
            """
            REPLY SET cloud settings of the TDBase:
            """
            _content_in_clear= '{};{};{};{};{};{};{};'.format(
                self.SETTINGS_REPLY,
                'reboot_en',
                'reboot_schedule_h',
                'reboot_schedule_m',
                'persistent_ping_en',
                'persistent_ping',
                'send_timeout'
            )
            _status_code = status.HTTP_200_OK
            return _content_in_clear, _status_code

        def net():
            """
            REPLY NET set TDBase network settings from cloud:
            """
            _content_in_clear= '{};{};{};{};{};{};{};'.format(
                self.NETWORK_REPLY,
                'DHCP_bool',
                'IP',
                'Subnet',
                'Gateway',
                'NTP',
                'DNS'
            )
            _status_code = status.HTTP_200_OK
            return _content_in_clear, _status_code

        replies = {
            self.REBOOT_REPLY: reb,
            self.ERROR_REPLY: err,
            self.OK_REPLY: non,
            self.SETTINGS_REPLY: set,
            self.NETWORK_REPLY: net,
            self.REL_REPLY: rel,
        }

        try:
            content_in_clear, status_code = replies[reply_type]()
            content_in_clear = '{}{}\0'.format(content_in_clear, self._generate_fill_data(content_in_clear))
            return HttpResponse(
                content=content_in_clear.encode('latin1'),
                status=status_code
            )
        except Exception as exc:
            return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def save_stampings(list_of_stampings, device):
        """
        TODO: restrutturare questa funzione con i nuovi dati
        :param list_of_stampings: lista di dizionari contenenti i dati delle stampings
        :param device:

        No return satatus code
        """

    @staticmethod
    def read_incoming_stamping(message):
        """
        Legge il messaggio in chiaro contenente le stampings e ne estrae i dati.

        :param message: body sottoforma di stringa in chiaro.
                Se il messaggio non contiene timbrature ritorna una lista vuota
        :return: Ritorna una lista di dizionari dove ogni dizionario rappresenta i dati contenuti in una Stamping.
                Le chiavi del dizionario sono quelle contenute nella stamping_params
        """

        stampings_list = []

        stamping_params = [
            'time',
            'badge',
            'direction',
            'code',
            'reading_point',
        ]

        try:
            stampings = message.split('""') if message is not None else []
            for row in stampings:
                data_stamping = row.replace('"', '').split(';')
                stamping_dictionary = {}
                for idx, val in enumerate(stamping_params):
                    stamping_dictionary[val] = data_stamping[idx]
                stampings_list.append(stamping_dictionary)

        except Exception as exc:
            pass

        return stampings_list

    @staticmethod
    def read_incoming_ping(message):
        """
        Legge il messaggio in chiaro contenente il ping e ne estrae i dati.
        :param message: Messaggio in chiaro contenente il ping nel formato ricevuto dal terminale

         TODO: salvare i dati estratti dal ping
         I dati sono salvati sottoforma di dizionario.
         Le chiavi del dizionario sono contenute in ping_settings_params
        """

        ping_settings_params = [
            'model',
            'reboot_en',
            'reboot_schedule_h',
            'reboot_schedule_m',
            'persistent_ping',
            'send_timeout',
            'DHCP_en',
            'IP_address',
            'SUBNET_mask',
            'GATEWAY_address',
            'NTP_address',
            'DNS_address'
        ]

        data_array = message.split(';')[1:]

        settings_dictionary = {}
        try:
            for idx, val in enumerate(ping_settings_params):
                settings_dictionary[val] = data_array[idx]
        except IndexError:
            pass

    def type_of_message(self, message):

        if str.startswith(message, self.PING_PREFIX):
            return self.PING
        else:
            return self.STAMPING

    @xframe_options_exempt
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        raw_body = request.body

        sn = request.META.get('HTTP_X_SERIAL_NUMBER', None)
        if not sn:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        device = True
        if not device:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        encryption = request.META.get('HTTP_X_ENCRIPTION', None)
        _binary = raw_body
        _cast = True

        if not encryption:
            encryption = request.META.get('HTTP_X_ENCRYPTION', None)
            try:
                _binary = b64string_to_binary(raw_body)
                print("DECODIFICATO <{}>".format(_binary))
            except Exception as exc:
                _binary = raw_body
            _cast = False
        if encryption == '0':
            data = _binary
        elif encryption == '1':
            k = b'2b7e151628aed2a6'
            data = Crypto(_binary, cast5_type=_cast, key=k)()
            if not data:
                return self._build_reply(self.ERROR_REPLY)
        else:
            return Response(status=status.HTTP_428_PRECONDITION_REQUIRED)

        try:
            data = data.decode("latin1")
        except Exception as exc:
            return self._build_reply(self.ERROR_REPLY)

        print('BODY:', data)
        message_type = self.type_of_message(data)

        def read_stampings():
            stampings_list = self.read_incoming_stamping(data)
            self.save_stampings(stampings_list, device)

        def read_ping():
            self.read_incoming_ping(data)

        readers = {
            self.PING: read_ping,
            self.STAMPING: read_stampings,
        }
        readers[message_type]()

        return self._build_reply(self.OK_REPLY)
