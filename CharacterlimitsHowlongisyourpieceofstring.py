# -*-coding:utf8 -*-
# author: yushan
# date: 2017-03-02

# 自己的解法
def charCheck(text, mx, spaces):
    length = len(text)
    if mx >= length:
        return [True,text]
    elif not spaces:
        con = text.replace(" ","")
        if len(con) <= mx:
            return [True,con]
        else:
            return [False,con[:mx]]
    else:
        return [False,text[:mx]]

def charCheck(text, mx, spaces):
    text = text if spaces else text.replace(' ', '')
    return [len(text) <= mx, text[:mx]]


def charCheck(text, mx, spaces):
    if spaces == False:
        text = ''.join(text.split())
    return [len(text)<=mx,text[:mx]]


# test.describe("Fixed Tests")
#
# test.it("should return OK if texts fit character count")
# test.assert_equals(charCheck("I am applying for the role of Base Manager on Titan.", 60, True),
#                    [True, "I am applying for the role of Base Manager on Titan."],
#                    "The input text length is below the character limit.")
# test.assert_equals(charCheck("I am looking to relocate to the vicinity of Saturn for family reasons.", 70, True),
#                    [True, "I am looking to relocate to the vicinity of Saturn for family reasons."],
#                    "The input text length is below the character limit.")
#
# test.it("should return true if texts fit character count, with spaces removed if needed")
# test.assert_equals(
#     charCheck("As Deputy Base Manager on Phobos for five Martian years, I have significant relevant experience.", 90,
#               False), [True, "AsDeputyBaseManageronPhobosforfiveMartianyears,Ihavesignificantrelevantexperience."],
#     "Did you remove the spaces?")
# test.assert_equals(
#     charCheck("A challenging career moment came with the rapid depletion of water supplies on Phobos.", 80, False),
#     [True, "AchallengingcareermomentcamewiththerapiddepletionofwatersuppliesonPhobos."], "Did you remove the spaces?")
#
# test.it("should not return true if texts do not fit character count")
# test.assert_not_equals(charCheck(
#     "Despite what some have suggested, this had nothing to do with the decorative fountains I had installed in my private quarters.",
#     100, False), [True,
#                   "Despite what some have suggested, this had nothing to do with the decorative fountains I had installed in my private quarters."],
#                        "The input text length is above the character limit.")
# test.assert_not_equals(
#     charCheck("Anyway what sort of society would we be if a Deputy Base Manager couldn't allow herself a few luxuries?",
#               70, False),
#     [True, "Anyway what sort of society would we be if a Deputy Base Manager couldn't allow herself a few luxuries?"],
#     "The input text length is above the character limit.")
#
# test.it("should not return true if texts do not fit character count, with spaces included if needed")
# test.assert_not_equals(charCheck("I swiftly resolved the situation with base-wide water rationing.", 60, True),
#                        [True, "I swiftly resolved the situation with base-wide water rationing."],
#                        "Did you count the spaces as characters?")
# test.assert_not_equals(
#     charCheck("After four Martian weeks of not washing, several colonists complained of the smell.", 80, True),
#     [True, "After four Martian weeks of not washing, several colonists complained of the smell."],
#     "Did you count the spaces as characters?")
#
# test.it("should return expected array if texts do not fit character count")
# test.assert_equals(
#     charCheck("But, as I pointed out, anyone complaining about standing downwind was lying. There was no wind.", 75,
#               True), [False, "But, as I pointed out, anyone complaining about standing downwind was lying"])
# test.assert_equals(charCheck("I have no notice period on Phobos. I can start immediately.", 50, True),
#                    [False, "I have no notice period on Phobos. I can start imm"],
#                    "Your array should include a shortened version of the original text.")
