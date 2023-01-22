
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

from pages.models import Page


def get_pages_middleware(get_response):

    def middleware(request):

        # application = get_wsgi_application()
        # pages = application.pages.objects.all().values
        pages = Page.objects.all().values

        response = get_response(request)
        if hasattr(response, 'data'):
            response.data['detail'] = 'bla-bla-bla'

        return response

    return middleware
