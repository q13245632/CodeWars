# 自己的解法
def in_array(array1, array2):
	string = "/".join(array2)
	lst = []
	for i in array1:
		if string.find(i) != -1 and i not in lst:
			lst.append(i)
	return sorted(lst)

# 一行代码
def in_array(a1, a2):
    return sorted(set(s1 for s1 in a1 if any(s1 in s2 for s2 in a2)))