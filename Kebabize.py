# 自己的解法
def kebabize(string):
    lst = []
    lst_num = []
    string_ch = "".join([x for x in string if x.isalpha()])
    for i in xrange(len(string_ch)):
        if string_ch[i].isupper() and string_ch[i].isalpha():
            lst_num.append(i)
    if len(lst_num) > 0:
        if lst_num[0] != 0:
            lst.append(string_ch[0:lst_num[0]].lower())
        for x in xrange(len(lst_num) - 1):
            lst.append(string_ch[lst_num[x]:lst_num[x+1]].lower())
        lst.append(string_ch[lst_num[len(lst_num)-1]:].lower())
    else:
        return string_ch
    return "-".join(lst)

# 简化程序
def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')
    
def kebabize(string):
    import re
    print(string)

    #Function to remove the numbers
    def trim_str(string):
        ans = ''.join([c for c in string if not c.isdigit()])
        return ans
    
    #Remove numbers
    tr_str = trim_str(string)

    test = re.sub('([a-z]*)([A-Z])', r'\1-\2', tr_str)
    
    #Check for empty string
    if not test: return test
    
    #Check for sequence of CAPS
    test2 = re.sub('([A-Z])([A-Z])', r'\1-\2', test)

    #Check for first char in string
    test3 = test2
    if test2[0]=='-': 
        test3 = test2[1:]
   
    #Convert to lowercase
    lo_str = re.sub('([a-z])([A-Z])', r'\1-\2', test3).lower()

    return(lo_str)