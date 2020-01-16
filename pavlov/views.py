from django.http import HttpResponse


def pavlov_home(request):
    """
    Return just a simple home message.
    """
    response = 'Pavlov Rest Api'
    return HttpResponse(response, content_type='text/html')
