from itertools import combinations


def count_combinations(items):
    for i in range(1, len(items) + 1):
        temp = len(items)
        l = 1
        for _ in range(i):
            l *= temp
            temp -= 1

        temp2 = 1
        r = 1
        for _ in range(i):
            r *= temp2
            temp2 += 1

        print(len(items), "C", i, "=", l, r, int(l / r))


def print_combinations(items):
    for i in range(1, len(items) + 1):
        for c in combinations(items, i):
            print(f'["{"\", \"".join(c)}"]')


if __name__ == '__main__':
    products = ['mv', 'machiney', 'plc', 'panel_board']
    print_combinations(products)
