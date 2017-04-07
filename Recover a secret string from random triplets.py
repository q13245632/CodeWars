def recoverSecret(triplets):
    res = ''
    while triplets != []:
        non_firsts = [num for t in triplets for num in t[1:]]
        firsts = [t[0] for t in triplets]
        for f in firsts:
            if f not in non_firsts:
                res += f
                for t in triplets:
                    if t[0] == f:
                        t.pop(0)
                break
        triplets = [t for t in triplets if t != []]
    return res


# Most Votes
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  
def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)