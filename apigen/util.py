import json
import random
from jinja2 import Template as jinja_template
from mako.template import Template as mako_template
from django.template import Template as django_template
from django.template import Context
from django.conf import settings
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


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
