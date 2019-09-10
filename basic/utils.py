import base64
from django.utils import timezone


def binary_to_b64_str(bin_image):
    if not bin_image:
        return None
    if not isinstance(bin_image, bytes):
        return None
    return base64.encodebytes(bin_image)


def b64string_to_binary(b64_string):
    if not b64_string:
        return None
    if not isinstance(b64_string, bytes) and isinstance(b64_string, str):
        b64_string = b64_string.encode("utf-8")
    return base64.decodebytes(b64_string)


def localize(dt):
    if hasattr(dt, "tzinfo"):
        tz = timezone.get_current_timezone()
        if dt.tzinfo is None:
            dt = timezone.make_aware(dt, tz)
        else:
            dt = timezone.localtime(dt, tz)
    return dt.replace(microsecond=0) if hasattr(dt, "hour") else dt


def daysOfThisMonth(**kwargs):
    """
        Restituisce il numero di giorni di un dato mese.
    :param kwargs:  date = DateTime or Date object
                    year = int(ANNO)
                    month = int(MESE)
    :return: int()
    """
    if len(kwargs) == 0:
        raise IndexError("method dayOfThisMonth called with 0 params (at least 1 expected)")
    date = kwargs.get("date", None)
    anno = kwargs.get("year", None)
    mese = kwargs.get("month", None)

    if date:
        data = date
    elif anno and mese:
        data = timezone.datetime(anno, mese, 1).date()
    else:
        raise ValueError("unknown values for method daysOfThisMonth")

    if isinstance(data, timezone.datetime):
        data = data.date()
    first = data.replace(day=1)
    _next = first + timezone.timedelta(days=33)
    last = _next.replace(day=1) - timezone.timedelta(days=1)
    return last.day