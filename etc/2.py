ary = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(4):
    for j in range(4):
        if i >= j:
            print('*', end=' ')
        else:
            print('  ', end=' ')
    print()

print()
for i in range(4,0,-1):
    for j in range(4):
        if i >= j :
            print('*', end=' ')
        else:
            print('  ', end='')
    print()

print()
for i in range(4):
    for j in range(3,-1,-1):
        if i >= j:
            print('*', end=' ')
        else:
            print('  ', end=' ')
    print()

print()
for i in range(4,0,-1):
    for j in range(4,0,-1):
        if i >= j:
            print('*', end=' ')
        else:
            print('  ', end=' ')
    print()
