# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14


def dirReduc(arr):
    lst = []
    for i in arr:
        if len(lst) <= 0:
            lst.append(i)
            continue
        if i == 'NORTH':
            if lst[-1:][0] == 'SOUTH':
                lst.pop()
            else:
                lst.append(i)
            continue
        if i == 'SOUTH':
            if lst[-1:][0] == 'NORTH':
                lst.pop()
            else:
                lst.append(i)
            continue
        if i == 'EAST':
            if lst[-1:][0] == 'WEST':
                lst.pop()
            else:
                lst.append(i)
            continue
        if i == 'WEST':
            if lst[-1:][0] == 'EAST':
                lst.pop()
            else:
                lst.append(i)
            continue
    return lst

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH", '').replace("SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST",
                                                                                                          '')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# test.assert_equals(dirReduc(a), ['WEST'])
# u=["NORTH", "WEST", "SOUTH", "EAST"]
# print dirReduc(u)
# test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])