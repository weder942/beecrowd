name = input()
salary = round(float(input()), 2)
sales = round(float(input()), 2)

print(f'TOTAL = R$ {salary+(sales*0.15):.2f}')