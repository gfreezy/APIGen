import json
import random
from jinja2 import Template as jinja_template
from mako.template import Template as mako_template
from django.template import Template as django_template
from django.template import Context
from django.conf import settings


settings.configure()

render_dict = {
    'jinja': jinja_template,
    'mako': mako_template,
    'django': django_template
    }


def change_dict(type_dict, immutable_dict):
    return_dict = {}
    for i, j in type_dict.items():
        if j == 'int':
            return_dict[i] = immutable_dict.get(i, type=int)
        else:
            return_dict[i] = immutable_dict.get(i)
    return return_dict


def check_dict(str_value):
    try:
        x = json.loads(str_value)
        if not isinstance(x, dict):
            str_value = ''
    except ValueError:
        str_value = ''


def render_args(engine_name, response, args):
    x = render_dict.get(engine_name)
    tem = x(response)
    if engine_name == 'django':
        return tem.render(Context(args))
    return tem.render(**args)


def sample_params(params):
    d = json.loads(params)
    new_d = {}
    for name, type_ in d.items():
        new_d.setdefault(name, sample_for_type(type_))

    return new_d


def sample_for_type(t):
    start = 1
    stop = 10
    if t == 'int':
        return random.randint(start, stop)

    elif t == 'string':
        text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'\
            .split(' ')

        start = random.randint(0, len(text))
        end = random.randint(start, len(text))
        return '%s.' % (' '.join(text[start:end]))
