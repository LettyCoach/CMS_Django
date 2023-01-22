

from django.utils import translation

# class TranslateMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):

#         print("custom middleware before next middleware/view--------------------")
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         translation.activate("fr")
#         response = self.get_response(request)

#         # Code to be executed for each response after the view is called
#         #
#         print("custom middleware after response or previous middleware+++++++++++++++++++++")

#         return response


def site_locale_middleware(get_response):

    def middleware(request):
        print('------------')
        translation.activate("fr")
        response = get_response(request)

        return response

    return middleware
