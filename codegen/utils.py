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

def capitalize(s: str) -> str:
    return s[0].upper() + s[1:]

def replace_all(olds:str, new: str, text:str) -> str:
    """replace all characters found in olds with the single character new in text"""
    if len(new) > 1:
        raise ValueError("new must be a single character")
    for char in text:
        if char in olds:
            text = text.replace(char, new)
    return text

def to_classname(s: str) -> str:
    s = replace_all("()", '', s)
    return capitalize(snake_to_camel(s))

def wrap(text,width):
    """used in mako templates for formatting"""
    return text.replace('\n','\n'+'\t'*width)