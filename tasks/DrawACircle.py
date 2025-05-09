def circle(radius):
    if radius == 0:
        return "\n"
    circle_str_list = []
    for y in range(-radius + 1, radius):
        for x in range(-radius + 1, radius):
            if x ** 2 + y ** 2 < radius ** 2:
                circle_str_list.append("#")
            else:
                circle_str_list.append(" ")
        circle_str_list.append("\n")
    return "".join(circle_str_list)