n = int(input('Enter Size Of Pyramid:'))
for x in range(1, n + 2):
    print('  ' * (n + 1 - x), end='')  # SPACES
    print("* " * (2 * x - 1))  # 2*N-1 STARS

for x in range(n, -1, -1):
    print('  ' * (n + 1 - x), end='')
    print("* " * (2 * x - 1))