# -*- encoding: utf-8 -*-
"""
@Project    :   SourceHub
@File       :   source_filters.py
@Time       :   2021/4/13 9:23
@Author     :   Thooooor
@Version    :   1.0
@Contact    :   thooooor999@gmail.com
@Describe   :   None
"""

from django import template

register = template.Library()


@register.filter(name='file_size')
def file_size(value):
    if value < 2 ** 10:
        return "%d B" % value

    if value < 2 ** 20:
        return "%.1f KB" % (value / (2 ** 10))

    if value < 2 ** 30:
        return "%.1f MB" % (value / (2 ** 20))

    return "%.1f GB" % (value / (2 ** 30))
