@dataclass
class ${obj.name}:
% for f in obj.fields:
    ${f.name}: ${f.type_ if f.type_ is not None else type(f.example).__name__}
    """${f.description}"""
% endfor