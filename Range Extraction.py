def solution(args):
	if not args:
		return ""
	lst = []
	item = []
	for x in xrange(0,len(args) - 1):
		if args[x+1] - args[x] == 1:
			item.append(str(args[x]))
			continue
		else:
			item.append(str(args[x]))
			if len(item) >= 3:
				lst.append("-".join([item[0],item[-1]]))
			else:
				lst.extend(item)
			item = []
	item.append(str(args[-1]))
	if len(item) >= 3:
		lst.append("-".join([item[0],item[-1]]))
	else:
		lst.extend(item)
	return ",".join(lst)

		


Test.describe("Sample Test Cases")

Test.it("Simple Tests")
Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,
	10,11,14,15,17,18,19,20]), 
	'-6,-3-1,3-5,7-11,14,15,17-20')
Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), 
	'-3--1,2,10,15,16,18-20')



def solution(args):
    lasts, r = [], []
    for a in args:
        r, lasts = (r + add(map(str, lasts)), [a]) if lasts and lasts[-1] + 1 != a else (r, lasts + [a])
    return ','.join(r + add(map(str, lasts)))
    
add = lambda e: [e[0]] if len(e) == 1 else [e[0], e[1]] if len(e) == 2 else [e[0] + '-' + e[-1]] 



def solution(args):
    rnge, ans = [], []
    for n1, n2 in zip(args, args[1:]+['']):
        if n1 + 1 == n2:
            if not rnge: rnge = [n1,n2]
            else:     rnge[1] = n2
            
        elif n1 + 1 != n2:
            if rnge:
                if rnge[0]+1 == rnge[1]: ans.extend( map(str,rnge) )
                else:           ans.append( '-'.join(map(str, rnge)) )
                rnge = []
            else:
                ans.append(str(n1))
                
    return ",".join(ans)