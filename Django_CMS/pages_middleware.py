
from pages.models import Page


class PageListMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        pages = Page.objects.all().values
        response.context_data["pages"] = pages
        return response
