from django.urls import path
from . import views


urlpatterns = [
    path('', views.PageListView.as_view(), name='pages_list'),
    # path("<slug:slug>", views.detail, name="pages_detail"),
    path("<slug:slug>", views.PageDetailView.as_view(), name="pages_detail"),
]
