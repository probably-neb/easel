<% tab = ' ' * 4%>\
class ${obj.name}(Base):
% if obj.description is not None and obj.description != "":
    """${obj.description}"""
% endif
    __tablename__ = '${obj.name_snake}'
% for field in obj.fields:
    % if field.is_enum:
    ${field.type_.enum_def()}
    ${field.enum_description}
    % endif
    ${field.name} = ${field.type_.sql_repr()}
    """${field.description} ${f"\n{tab*2}Example: {field.example}" if field.example is not None else ""}"""
% endfor\