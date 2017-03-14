# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-14


def to_camel_case(text):
    if text == "" or len(text) <= 0:
        return ""
    first = -1
    string = text[0]
    for i in xrange(1,len(text)):
        if first == 0 and text[i].isalpha():
            string += text[i].upper()
            first = -1
        elif not text[i].isalpha():
            first = 0
        else:
            string += text[i]
    return string


def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s


def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''
# test.describe("Testing function to_camel_case")
# test.it("Basic tests")
# test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")