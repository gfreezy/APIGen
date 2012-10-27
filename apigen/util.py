from jinja2 import Template as jinja_template
from mako.template import Template as mako_template

render_dict = {
    'jinja':jinja_template,
    'mako':mako_template
    }


def change_dict(type_dict, immutable_dict):
    return_dict = {}
    for i,j in type_dict.items():
        if j == 'int':
            return_dict[i] = immutable_dict.get(i, type=int)
        else:
            return_dict[i] = immutable_dict.get(i)

    return return_dict

def dump_dict(str_value):
    if not (str_value.find(',') and str_value.find(':')):
        return {}
    result = {}
    params = str_value.split(',')
    for item in params:
        if not item.find(':'):
            return {}
        result[item.split(':')[0]] = item.split(':')[1]
    return result

def render_args(engine_name, response, args):
    x = render_dict.get('jinja')
    tem = x(response)
    return tem.render(**args)

