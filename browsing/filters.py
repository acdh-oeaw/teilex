import django_filters
from dal import autocomplete
from words.models import Word
from vocabs.models import SkosConcept

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class WordListFilter(django_filters.FilterSet):

    orth = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Transkription"
        )

    class Meta:
        model = Word
        fields = [
            'legacy_id', 'orth'
        ]
