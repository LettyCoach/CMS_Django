from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Page
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.utils import translation
from django.template import loader


def dispatch_view(request, slug):
    if slug == "admin":
        return redirect("/admin/")
    elif slug == "news":
        return redirect("/news/")
    else:
        return PageDetailView.as_view()(request, slug=slug)


class PageListView(ListView):
    model = Page
    template_name = "pages/list.html"


class PageDetailView(TemplateView):
    template_name = 'pages/detail.html'

    def get_context_data(self, slug, *args, **kwargs):
        domain = self.request.META['HTTP_HOST']
        lang = domain[0:2]
        page = Page.objects.get(slug=slug)
        comments = page.pComments.filter(lang=lang).values
        context = super(PageDetailView, self).get_context_data(*args, **kwargs)
        context['object'] = {
            'page': page,
            'comments': comments
        }
        return context
