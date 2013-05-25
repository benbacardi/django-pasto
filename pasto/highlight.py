"""Highlighting options for Pasto"""
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight

LEXERS = (
    ('bash', 'Bash'),
    ('c', 'C'),
    ('css', 'CSS'),
    ('diff', 'Diff'),
    ('django', 'Django/Jinja'),
    ('html', 'HTML'),
    ('irc', 'IRC logs'),
    ('js', 'JavaScript'),
    ('perl', 'Perl'),
    ('php', 'PHP'),
    ('pycon', 'Python console session'),
    ('pytb', 'Python Traceback'),
    ('python', 'Python'),
    ('python3', 'Python 3'),
    ('sql', 'SQL'),
    ('text', 'Text only'),
)

DEFAULT_LEXER = 'python'

def highlight_object(code):
    """
    Returns HTML-formatted highlighted code.
    """
    return highlight(code.code, get_lexer_by_name(code.lexer), HtmlFormatter())
