def is_unique(x):
    if x == []:
        return True
    else:
        y = x.pop()
        if y in x:
            return False
        else:
            return is_unique(x)


def triangle_shape(height):
    s = "x"
    esp = " "
    if height == 0:
        return ""
    return "\n".join(
        [
            (height - 1 - i) * esp + (2 * i + 1) * s + (height - 1 - i) * esp
            for i in range(height)
        ]
    )
