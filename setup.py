"""
Zephir syntax highlighting for Pygments.
"""

from setuptools import setup

entry_points = """
[pygments.lexers]
zephir = zephir.zephir:ZephirLexer
"""

setup(
    name         = 'zephir',
    version      = '0.2',
    description  = __doc__,
    author       = "Phalcon Team",
    packages     = ['zephir'],
    entry_points = entry_points
)
