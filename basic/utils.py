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
