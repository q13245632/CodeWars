# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-04-08

def strip_url_params(url, params_to_strip = []):
    if "?" in url:
        main_url,params = url.split("?")
    else:
        return url
    items = params.split("&")
    later_items = []
    s = []
    for x in items:
        x_item = x.split("=")
        if params_to_strip and x_item[0] in params_to_strip:
            continue
        if x_item[0] in s:
            continue
        else:
            later_items.append(x)
            s.append(x_item[0])
    if later_items:
        return main_url + "?" + "&".join(later_items)
    else:
        return main_url


print strip_url_params('www.codewars.com?a=1&b=2&a=2')


def strip_url_params(url, param_to_strip=[]):
    if '?' not in url:
        return url

    queries = (url.split('?')[1]).split('&')
    queries_obj = [query[0] for query in queries]
    for i in range(len(queries_obj) - 1, 0, -1):
        if queries_obj[i] in param_to_strip or queries_obj[i] in queries_obj[0:i]:
            queries.pop(i)

    return url.split('?')[0] + '?' + '&'.join(queries)