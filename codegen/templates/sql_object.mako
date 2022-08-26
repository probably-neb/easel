<% tab = ' ' * 4%>
class ${obj.name}(Base):
% if obj.description is not None and obj.description != "":
    """${obj.description}"""
% endif
    __tablename__ = '${obj.name_snake}'
% for field in obj.fields:
    % if field.option_enum is not None:
    ${field.option_enum.name} = enum.Enum('${field.option_enum.name}', ${field.option_enum.values})
    """Enum for the allowed values of the ${field.name} field"""
    % endif
    ${field.name} = ${field.init.sql_repr()}
    """${field.description} ${f"\n{tab*2}Example: {field.example}" if field.example is not None else ""}"""
% endfor