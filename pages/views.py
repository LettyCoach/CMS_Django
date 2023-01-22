from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import translation
from django.conf import settings
from django.views.generic import ListView, DetailView
# from django.utils.translation import gettext as _
from .models import Page


def index(request):

    pages = Page.objects.all().values
    context = {
        'pages': pages
    }
    template = loader.get_template('pages/index.html')

    return HttpResponse(template.render(context, request))


def detail(request, slug):
    domain = request.META['HTTP_HOST']
    lang = domain[0:2]
    page = Page.objects.get(slug=slug)
    comments = page.pComments.filter(lang=lang).values
    context = {
        'object': page,
        'comments': comments
    }
    template = loader.get_template('pages/detail.html')
    return HttpResponse(template.render(context, request))


class PageListView(ListView):
    model = Page
    template_name = "pages/list.html"


# class PageDetailView(DetailView):
#     model = Page
#     template_name = "pages/detail.html"
