from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import New
from pages.models import Comment


def index(request):
    template = loader.get_template('news/index.html')
    return HttpResponse(template.render({}, request))

def detail(request, slug):
    domain = request.META['HTTP_HOST']
    lang = domain[0:2]
    new = New.objects.get(slug=slug)
    comments = new.nComments.filter(lang=lang).values
    context = {
        'object': new,
        'comments': comments
    }
    template = loader.get_template('news/detail.html')
    return HttpResponse(template.render(context, request))


class NewListView(ListView):
    model = New
    template_name = 'news/list.html'


# class NewDitailView(DetailView):
#     model = New
#     template_name = 'news/detail.html'
