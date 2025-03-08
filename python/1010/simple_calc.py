a, b, c = map(float, input().split())
a2, b2, c2 = map(float, input().split())

print(f'VALOR A PAGAR: R$ {(int(b)*float(c))+(int(b2)*float(c2)):.2f}')
