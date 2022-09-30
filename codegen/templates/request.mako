<%page args="req"/>\
<%! from utils import wrap %>
        def ${req.name}(${req.param_repr()}) -> ${req.return_type.py_repr()}:
            """
            description: ${wrap(req.description, 6)}
            summary: ${req.summary}

            % for param in req.parameters:
            :param ${param.type_.py_repr()} ${param.name}: ${wrap(param.description, 6)}
            % endfor
            """

            endpoint = f'${req.endpoint}'
            res = requests.${req.method.lower()}(endpoint, header=header, params=params)
            return res.json()