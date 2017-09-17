from django.db import models
from vocabs.models import SkosConcept
from bib.models import Book


class Word(models.Model):
    legacy_id = models.CharField(blank=True, max_length=250)
    word_type = models.ForeignKey(SkosConcept, blank=True, null=True, related_name='word_type')
    language = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='word_language'
    )
    orth = models.CharField(blank=True, max_length=250)
    has_form = models.ManyToManyField(
        'Word', blank=True, related_name="is_form"
    )
    has_sense = models.ManyToManyField(
        'Word', blank=True, related_name="is_sense"
    )
    has_gram = models.ManyToManyField(
        'Word', blank=True, related_name="is_gram"
    )
    reference = models.ManyToManyField(
        Book, blank=True, related_name="wordform_reference"
    )
    pos = models.ForeignKey(SkosConcept, blank=True, null=True, related_name='word_pos')
    morph_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='word_morph_type'
    )
    gender = models.ForeignKey(SkosConcept, blank=True, null=True, related_name='word_gender')
    subc = models.ForeignKey(SkosConcept, blank=True, null=True, related_name='word_subc')
    usg = models.ForeignKey(SkosConcept, blank=True, null=True, related_name='word_usg')
    arguments = models.CharField(blank=True, max_length=250)

    def get_next(self):
        next = Word.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Word.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('words:word_detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{} ({})".format(self.orth, self.word_type)
