n, m = map(int, input().split())      #спиздит 5 #разновидность купюр 2
nominals = sorted(list(map(int, input().split())))  #две купюры по 1 и две 2

k = 0
amount = 0
result = []
for i in range(m):
    sort_nominals = nominals * 2
    sort_nominals.sort()
    sort_nominals = list(reversed(sort_nominals))
    if n == 0:
        print(k)
        print(' '.join(map(str, result)))
        break
    elif n < 0:
        print(-1)
    elif n > 0 and k == len(sort_nominals):
        print(-1)

    for y in sort_nominals:
        n = n - y
        k += 1
        result += [y]
        if n > 0:
            continue
        else:
            break


