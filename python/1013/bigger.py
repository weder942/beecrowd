a, b, c = map(int, input().split())


def bigger(a, b):
    return (a + b + abs(a - b)) // 2


print(f'{bigger(bigger(a, b), c)} eh o maior')
