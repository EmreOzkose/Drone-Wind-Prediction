#
#
# Yunusemre Ozkose
# 19.11.21
#

import time
import datetime


def date2timestamp(s):
    formatted = f"{s[0:4]}-{s[4:6]}-{s[6:8]} {s[8:10]}:{s[10:12]}:{s[12:14]}"
    return time.mktime(datetime.datetime.strptime(formatted, "%Y-%m-%d %H:%M:%S").timetuple())
