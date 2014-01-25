# Based on pygments documentation
from __future__ import print_function

import re
import copy

from pygments.lexer import RegexLexer, ExtendedRegexLexer, bygroups, using, include, this
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Other, Punctuation, Literal
from pygments.util import get_bool_opt, get_list_opt, looks_like_xml, html_doctype_matches
from pygments.lexers.agile import RubyLexer
from pygments.lexers.compiled import ScalaLexer

class ZephirLexer(RegexLexer):
    """
    For Zephir language
    """

    name = 'Zephir'
    aliases = ['zephir']
    filenames = ['*.zep']

    zephir_keywords = [ 'fetch', 'echo', 'isset', 'empty']
    zephir_type = [ 'bit', 'bits' , 'string' ]

    flags = re.DOTALL
    tokens = {
        'commentsandwhitespace': [
            (r'\s+', Text),
            (r'//.*?\n', Comment.Single),
            (r'/\*.*?\*/', Comment.Multiline)
        ],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            (r'/(\\.|[^[/\\\n]|\[(\\.|[^\]\\\n])*])+/'
             r'([gim]+\b|\B)', String.Regex, '#pop'),
            (r'', Text, '#pop')
        ],
        'badregex': [
            (r'\n', Text, '#pop')
        ],
        'root': [
            (r'^(?=\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            (r'\+\+|--|~|&&|\?|:|\|\||\\(?=\n)|'
             r'(<<|>>>?|==?|!=?|->|[-<>+*%&\|\^/])=?', Operator, 'slashstartsregex'),
            (r'[{(\[;,]', Punctuation, 'slashstartsregex'),
            (r'[})\].]', Punctuation),
            (r'(for|in|while|do|break|return|continue|switch|case|default|if|else|loop|require|inline|'
             r'throw|try|catch|finally|new|delete|typeof|instanceof|void|namespace|use|extends|'
             r'this|fetch|isset|unset|echo|fetch|likely|unlikely|empty)\b', Keyword, 'slashstartsregex'),
            (r'(var|let|with|function)\b', Keyword.Declaration, 'slashstartsregex'),
            (r'(abstract|boolean|bool|char|class|const|double|enum|export|'
             r'extends|final|float|goto|implements|import|int|string|interface|long|ulong|char|uchar|native|unsigned|'
             r'private|protected|public|short|static|self|throws|reverse|'
             r'transient|volatile)\b', Keyword.Reserved),
            (r'(true|false|null|undefined)\b', Keyword.Constant),
            (r'(Array|Boolean|Date|_REQUEST|_COOKIE|_SESSION|'
             r'_GET|_POST|_SERVER|this|stdClass|range|count|iterator|'
             r'window)\b', Name.Builtin),
            (r'[$a-zA-Z_][a-zA-Z0-9_\\]*', Name.Other),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }


if __name__ == '__main__':
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter, Terminal256Formatter
    from pygments.formatters import RawTokenFormatter
    from sys import argv

    if len(argv) > 1:
        import io

        for arg in argv[1:]:
            input = io.open(arg, 'r')
            code = input.read(-1)
            print("Highlighting " + arg)
            #print(highlight(code, MyDiffLexer(encoding='chardet'),
            #      HtmlFormatter(encoding='utf-8')))
            print(highlight(code, ZephirLexer(encoding='chardet'),
                  Terminal256Formatter(encoding='utf-8')))

    else:
        code = """
def FeatureFPU : SubtargetFeature<"fpu", "fpu", "true",
    "Enable FPU">;
""";
        print(highlight(code, ZephirLexer(), Terminal256Formatter()))
