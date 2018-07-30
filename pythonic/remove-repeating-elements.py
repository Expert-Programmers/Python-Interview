def remove_repeating_elements(l: list) -> list:
    return list(set(l))


def remove_repeating_elements_(l: list) -> list:
    d = {}
    for e in l:
        d[e] = 1
    return list(d.keys())


if __name__ == '__main__':
    l = [1, 1, 2, 3, 2, 3, 1, 1]
    print(remove_repeating_elements(l))
    print(remove_repeating_elements_(l))
