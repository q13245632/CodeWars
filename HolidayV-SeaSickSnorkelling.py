def sea_sick(sea):
    n = 0
    for x in xrange(len(sea) - 2):
        print sea[x+1:x+2], "++" ,sea[x+2:x+3]
        if sea[x+1:x+2] != sea[x+2:x+3]:
            n += 1
    print n
    print int(0.2 * len(sea))
    print len(sea)
    if n > int(0.2 * len(sea)):
        return "Throw Up"
    else:
        return "No Problem"