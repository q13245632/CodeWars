# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-16

import sys
def cakes(recipe, available):
    max_cake = sys.maxint
    for k,v in recipe.items():
        if not available.__contains__(k):
            return 0
        else:
            n = available[k] // v
            max_cake = max_cake if max_cake < n else n
    return max_cake

def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)

# test.describe('Testing Pete, the Baker')
# test.it('gives us the right number of cakes')
#
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# test.assert_equals(cakes(recipe, available), 2, 'Wrong result for example #1')
#
# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# test.assert_equals(cakes(recipe, available), 0, 'Wrong result for example #2')