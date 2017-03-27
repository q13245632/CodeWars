# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-27


def pick_peaks(arr):
    res = {}
    pos = []
    peaks = []
    lst = []
    pos_item = 0
    cycle = True
    for i in xrange(len(arr)):
        if lst:
            last = lst[-1]
            if arr[i] > last:
                pos_item = i
                cycle = True
                lst.append(arr[i])
            elif arr[i] == last:
                cycle = True
                continue
            elif cycle:
                cycle = False
                if i-1 == 0 or i - 1 == len(arr)-1:
                    continue
                pos.append(pos_item)
                peaks.append(last)
            else:
                lst.append(arr[i])
                pos_item = i
        else:
            lst.append(arr[i])
    res["pos"] = pos
    res["peaks"] = peaks
    return res

def pick_peaks(arr):
    pos = []
    peaks = []
    for i in xrange(1, len(arr)-1):
        if arr[i] > arr[i-1]:
            for j in xrange(i+1, len(arr)):
                if arr[j] > arr[i]:
                    break
                elif arr[j] < arr[i]:
                    pos += [i]
                    peaks += [arr[i]]
                    break
    return {'pos': pos, 'peaks': peaks}


def pick_peaks(arr):
    peak, pos = [], []
    res = {"peaks": [], "pos": []}

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak, pos = [arr[i]], [i]

        elif arr[i] < arr[i - 1]:
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []

    return res