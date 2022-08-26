import re

def depluralize(word: str) -> str:
    if word.endswith('s'):
        word = word[:-1]
    return word

def pluralize(word: str) -> str:
    if not word.endswith('s'):
        word += 's'
    return word


_underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_underscorer2 = re.compile(r'([a-z0-9])([A-Z])')

def camel_to_snake(s: str) -> str:
    """
    Convert camel-case to snake-case in python.
    e.g.: CamelCase -> snake_case
    Relevant StackOverflow question: http://stackoverflow.com/a/1176023/293064
    __author__ = 'Jay Taylor [@jtaylor]'

    Is it ironic that this function is written in camel case, yet it
    converts to snake case? hmm..
    """
    subbed = _underscorer1.sub(r'\1_\2', s)
    return _underscorer2.sub(r'\1_\2', subbed).lower()

def snake_to_camel(s: str) -> str: #also with first letter capitalized
    first, *words = s.split('_')
    subbed = ''.join([first.lower(), *map(str.title, words)])
    return subbed

def take_longer(a: str, b: str) -> str:
    if b is None or (a is not None and len(a) > len(b)):
        return a
    return b