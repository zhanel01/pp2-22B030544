a = set(1, 2, 3, 4, 5, 6, 7, 8 ,9)
N= int(input())

for i in range(N) :
    s = input().split(' ')
    command = s[0]

    if command == "pop" :
        a.pop()
    elif command == 'remove' :
        value = int(s[1])
        a.remove(value)
    elif command == 'discart' :
        value =int(s[1])
        a.discart(value)

print(sum(a))

    