#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhangchangming'

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    tz = re.match(r'UTC([\+\-][01]?[0-9]):', tz_str)
    utc = 0
    if tz:
        utc = int(tz.group(1))
    else:
        return -1

    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    cday = cday.replace(tzinfo=timezone(timedelta(hours=utc)))
    return cday.timestamp()

# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
