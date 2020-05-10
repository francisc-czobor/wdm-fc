from django import template
from urllib.parse import urlencode

register = template.Library()


def get_params(**kwargs):
    safe_args = {key: kwargs[key] for key in kwargs.keys() if kwargs[key] is not None}
    if safe_args:
        return '?{}'.format(urlencode(safe_args))
    return ''


register.simple_tag(get_params, name='get_params')
