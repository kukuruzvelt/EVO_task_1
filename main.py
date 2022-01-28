directions = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}


def direction(facing, turn):
    if facing not in directions.keys():
        raise ValueError("Wrong facing")
    if turn % 45 != 0 or -1080 > turn > 1080:
        raise ValueError("Wrong turn")
    return __simp_facing(directions.get(facing) + turn)


def __simp_facing(num):
    if num > 0:
        while num >= 360:
            num -= 360
    elif num < 0:
        while num < 360:
            num += 360
        num = 360 - num
    return __get_key(num)


def __get_key(turn):
    for k in directions.keys():
        if directions.get(k) == turn:
            return k



