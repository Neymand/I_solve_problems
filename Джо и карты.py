a = int(input())

user1 = input()
joy = list(map(int, user1.split()))
user2 = input()
win = list(map(int, user2.split()))

ram = joy.copy()
ind = 0
diapazon = []

if joy == win:
    print("YES")
else:

    for i in ram:
        index = ram.index(i)
        while ind != a:
            if i != win[ind]:

                diapazon += [index]
                ram[index] = '*'
                ind += 1

                break
            else:
                ram[index] = '*'
                ind += 1
                break

    new_diapazon = diapazon[:1] + diapazon[-1:]

    start = new_diapazon[0]
    end = new_diapazon[1]

    ind = 1
    sub = joy[start:end+1]
    sub2 = win[start:end+1]
    sub.reverse()

    if sorted(sub) == sub2:
        for i in sub2:
            if ind == len(sub):
                print('YES')
                break
            if i > sub2[ind]:
                print('NO')
                break
            else:
                ind += 1
            #print('Yes')
    else:
        print("NO")
