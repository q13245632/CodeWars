# -*-coding:utf8 -*-
# author: yushan
# date: 2017-02-26


# 自己的解法
import string
def to_nato(words):
    strings = []
    letters = list(string.uppercase)
    word_lst = ['Alfa','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliett','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whiskey','Xray','Yankee','Zulu']
    for i in words.upper():
        if ord('A') <= ord(i) <= ord('Z'):
            strings.append(word_lst[ord(i) - ord('A')])
        elif ord(i) != 32:
            strings.append(i)
    return " ".join(strings)


def to_nato(words):
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')

import string

db = { 'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',
       'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett',
       'K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar',
       'P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango',
       'U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee',
       'Z':'Zulu'
      }

def to_nato(words):
    words = words.replace(' ','').upper()
    return ' '.join([db[i] if i in db else i for i in list(words)])


to_nato("If you can read")
to_nato("Q.QH")
# Quebec . Quebec Hotel
# Test.describe("Basic Tests")
# Test.assert_equals(to_nato('If you can read'), "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
# Test.assert_equals(to_nato('Did not see that coming'), "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")