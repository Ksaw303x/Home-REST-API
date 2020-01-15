from django.http import HttpResponse


def alexa_home(request):
    """
    Return just a simple home message.
    """
    response = 'alexa-skill-home'
    return HttpResponse(response, content_type='text/html')
