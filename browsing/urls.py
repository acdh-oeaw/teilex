from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'words/$', views.WordListView.as_view(), name='browse_words'),
]
