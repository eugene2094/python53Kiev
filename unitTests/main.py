def add(*args, **kwargs):
    result = 0
    for elem in list(args) + list(kwargs.values()):
        if isinstance(elem, (int, float, bool)):
            result += elem
        else:
            try:
                result += float(elem)
                continue
            except (ValueError, TypeError):
                pass
    return result


def devide(*args, **kwargs):
    result = 0
    for elem in args:
        result += elem

    for elem in kwargs.values():
        result += elem
    return result
