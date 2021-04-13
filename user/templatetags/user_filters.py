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
import math

from django import template
from django.utils import timezone

register = template.Library()


@register.filter(name='timesince_zh')
def time_since_zh(value):
    now = timezone.now()
    diff = now - value

    if diff.days == 0 and 0 <= diff.seconds < 60:
        return '刚刚'

    if diff.days == 0 and 60 <= diff.seconds < 3600:
        return str(math.floor(diff.seconds / 60)) + "分钟前"

    if diff.days == 0 and 3600 <= diff.seconds < 86400:
        return str(math.floor(diff.seconds / 3600)) + "小时前"

    return value
