from django.views.generic.detail import DetailView
from .models import Word


class WordDetailView(DetailView):

    model = Word
    template_name = 'words/word_detail.html'
