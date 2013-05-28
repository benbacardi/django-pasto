"""Django app!"""
from django.db import models
from django.contrib.auth.models import User

import string
import random
import datetime

from .utils import get_diff
from .highlight import DEFAULT_LEXER, LEXERS, highlight_object

class Code(models.Model):
    slug = models.SlugField(max_length=10, blank=True, db_index=True)
    title = models.CharField(max_length=160)
    author = models.ForeignKey(User, blank=True, null=True, related_name='code_pastes')
    code = models.TextField()
    lexer = models.CharField(max_length=20, choices=LEXERS, default=DEFAULT_LEXER)
    created = models.DateTimeField(default=datetime.datetime.now)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='revisions')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Code Paste'
        verbose_name_plural = 'Code Pastes'

    def __uncode__(self):
        return '%s (%s)' % self.title, self.slug

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = generate_unique_slug(max_length=10) or self.pk
        super(Code, self).save(*args, **kwargs)

    def highlight(self):
        """
        Returns the HTML-formatted highlighted code.
        """
        return highlight_object(self)

    def diff(self, code):
        """
        Returns a friendly-format diff of the two code objects.
        """
        one, two = self, code
        if self.created >= code.created:
            one, two = two, one
        return get_diff(one, two)

def generate_unique_slug(min_length=4, max_length=10, attempts=10):
    """
    Returns a unique slug between min_length and max_length characters.
    """
    choice = generate_slug(min_length, max_length)
    while Code.objects.filter(slug=choice).exists() and attempts > 0:
        choice = generate_slug(min_length, max_length)
        attempts = attempts - 1
    return choice if attempts else None
        
def generate_slug(min_length, max_length):
    """
    Returns a slug between min_length and max_length characters.
    """
    choices = string.ascii_letters + string.digits
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(choices) for x in xrange(length))
