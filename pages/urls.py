from django.urls import path
from . import views


urlpatterns = [
    path('', views.PageListView.as_view(), name='pages_list'),
    path("<slug:slug>", views.dispatch_view, name='dispatch')
]
