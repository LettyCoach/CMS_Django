from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.NewListView.as_view(), name='news_list'),
    path("<slug:slug>", views.NewDetailView.as_view(), name='news_detail'),
    # path("<slug:slug>", views.NewDitailView.as_view(), name='news_detail'),
]
