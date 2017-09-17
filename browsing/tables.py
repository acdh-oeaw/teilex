import django_tables2 as tables
from django_tables2.utils import A
from words.models import *


class WordTable(tables.Table):
    orth = tables.LinkColumn(
        'words:word_detail',
        args=[A('pk')], verbose_name='Word'
    )
    word_type = tables.RelatedLinkColumn()
    pos = tables.RelatedLinkColumn()

    class Meta:
        model = Word
        sequence = ('legacy_id', 'orth', 'pos', 'word_type')
        attrs = {"class": "table table-responsive table-hover"}
