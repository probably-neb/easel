${name}_params = {
% for param in parameters:
    "${param.parameter}": {
        """${param.description}"""
        "type": "${param.type_}",
        "required": ${param.required},
        "allowed_values": ${param.allowed_values},
    },
% endfor
}
<% 
    params = []
    needs = []
    params_str = ""
    needs_str = ""
    for p in parameters:
        pstr = p.parameter
        if "[]" in pstr:
            pstr += ": list"
            pstr = pstr.replace("[]", "")
        elif "id" in pstr:
            pstr += ": int"
        if p.required:
            params.insert(0, pstr)
        else:
            pstr += "=None"
            params.append(pstr)
    for n in needs:
        if "id" in n:
            n += ": int"
        needs.append(n)
    if params:
        needs.append("")
    params_str = ", ".join(params)
    needs_str = ", ".join(needs)
 %>

# ${method}
def ${name}(${needs_str}${params_str}):
    """${description}"""
    params = locals().copy()
    % for n in needs:
    del params["${n}"]
    % endfor

    endpoint = f'${endpoint}'
    res = requests.${method.lower()}(endpoint, header=header, params=params)
    return res.json()