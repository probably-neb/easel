@dataclass
class ${obj.name}:
% for f in obj.fields:
    ${f.name}: ${f.init.py_repr()}
    """${f.description}"""
% endfor