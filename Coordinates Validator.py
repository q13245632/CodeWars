# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-27


def is_valid_coordinates(coordinates):
    print coordinates
    lst = coordinates.split(",")
    if not len(lst) == 2:
        return False
    try:
        a,b = lst[0],lst[1]
        if not "e" in a and not "e" in b and -90.0<=float(a.strip())<=90.0 and -180.0<=float(b.strip())<=180.0:
            return True
        else:
            return False
    except ValueError:
        return False
    return True

def is_valid_coordinates(coordinates):
    try:
        lat, lng = [abs(float(c)) for c in coordinates.split(',') if 'e' not in c]
    except ValueError:
        return False

    return lat <= 90 and lng <= 180