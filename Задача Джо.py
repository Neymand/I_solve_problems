col_sum = input().split()
col = int(col_sum[0])
sum = int(col_sum[1])
price = input().split()
i = 0
result = 0
while i != col:
    if int(price[i]) > sum:
        pass
    if int(price[i]) < sum and int(price[i]) > result:
        result = int(price[i])
    if int(price[i]) == sum and int(price[i]) > result:
        result = int(price[i])
    i += 1
print(result)
