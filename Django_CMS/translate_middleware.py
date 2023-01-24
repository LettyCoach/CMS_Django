

from django.utils import translation


class TranslateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        domain = request.META['HTTP_HOST']
        lang = domain[0:2]
        translation.activate(lang)
        response = self.get_response(request)
        return response
