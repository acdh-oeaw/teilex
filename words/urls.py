from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^word/(?P<pk>[0-9]+)$', views.WordDetailView.as_view(),
        name='word_detail'),
]
