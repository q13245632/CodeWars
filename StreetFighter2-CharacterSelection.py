# -*-coding:utf8 -*-
# 自己的解法
def street_fighter_selection(fighters, initial_position, moves):
    a,b = initial_position
    lst = []
    for i in moves:
        if i == "up":
            if a == 0:
                lst.append(fighters[a%2][b%6])
            else:
                a -= 1
                lst.append(fighters[a%2][b%6])
        if i == "down":
            if a == 0:
                a += 1
                lst.append(fighters[a%2][b%6])
            else:
                lst.append(fighters[a%2][b%6])
        if i == "left":
            b -= 1
            b += 6
            lst.append(fighters[a%2][b%6])
        if i == "right":
            b += 1
            lst.append(fighters[a%2][b%6])
    return lst

# 测试集
# fighters = [
# 	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
# 	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# opts = ["up","down","right","left"]
#
# test.describe("Character selection")
# test.it("should work with no selection cursor moves")
# moves =  []
# solution = []
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
#
# test.it("should go left 8 times")
# moves =  ["left"]*8
# solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
#
# test.it("should go right 8 times")
# moves =  ["right"]*8
# solution = ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
#
# test.it("should go up 4 times, always the same")
# moves =  ["up"]*4
# solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
#
# test.it("should go down 4 times, always the same")
# moves =  ["down"]*4
# solution = ['Ken', 'Ken', 'Ken', 'Ken']
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
#
# test.it("should use all 4 directions counter-clockwise twice")
# moves =  ["down","right","up","left"]*2
# solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
#
# test.it("should use all 4 directions clockwise twice")
# moves =  ["up","left","down","right"]*2
# solution = ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)
#
# test.it("should cover all characters")
# moves =  ["up"]+["left"]*6+["down"]+["right"]*6
# solution = ['Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Ken']
# test.assert_equals(street_fighter_selection(fighters,(0,0), moves), solution)

# 其他解法
MOVES = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

def street_fighter_selection(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dy, dx = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters):
            y -= dy
        x = (x + dx) % len(fighters[y])
        hovered_fighters.append(fighters[y][x])
    return hovered_fighters


