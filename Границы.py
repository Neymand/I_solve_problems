a = int(input())
b = int(input())

i = True

while True:
    c = input()
    if c == '':
        print(i)
        break
    elif int(c) >= a and int(c) <= b:
        i = True
    elif int(c) <= a or int(c) >= b:
        i = False



