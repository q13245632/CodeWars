# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-23


def format_duration(seconds):
    h_more,m_more = divmod(seconds,3600)
    d_more,h = divmod(h_more,24)
    y,d = divmod(d_more,365)
    m,s = divmod(m_more,60)
    lst = []
    if y >= 1:
        y_str = "1 year" if y == 1 else str(y) + " years"
        lst.append(y_str)
    if d >= 1:
        d_str = "1 day" if d == 1 else str(d) + " days"
        lst.append(d_str)
    if h >= 1:
        h_str = "1 hour" if h == 1 else str(h) + " hours"
        lst.append(h_str)
    if m >= 1:
        m_str = "1 minute" if m == 1 else str(m) + " minutes"
        lst.append(m_str)
    if s >= 1:
        s_str = "1 second" if s == 1 else str(s) + " seconds"
        lst.append(s_str)
    if not lst:
        lst = "now"
    else:
        last = lst[-1]
        if len(lst) > 1:
            lst = ", ".join(lst[:-1])
            lst += " and " + last
        else:
            lst = last
    return lst


times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]