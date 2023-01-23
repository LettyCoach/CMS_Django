from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import New
from pages.models import Comment


class NewListView(ListView):
    model = New
    template_name = 'news/list.html'


class NewDetailView(TemplateView):
    template_name = 'news/detail.html'

    def get_context_data(self, slug, *args, **kwargs):
        domain = self.request.META['HTTP_HOST']
        lang = domain[0:2]
        new = New.objects.get(slug=slug)
        comments = new.nComments.filter(lang=lang).values
        context = {
            'new': new,
            'comments': comments
        }
        context = super(NewDetailView, self).get_context_data(*args, **kwargs)
        context['object'] = {
            'new': new,
            'comments': comments
        }
        return context
