import math

from django import template

register = template.Library()


def even(value):
    i = value % 10
    count = 0
    while value != 0:
        if i % 2 == 0:
            count += 1
        value = math.floor(value / 10)
        i = value % 10
    return count


register.filter('even_no_count', even)
