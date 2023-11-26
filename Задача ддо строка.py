stroka = input()
word = 'sheriff'
dic = {'s': 1, 'h': 1, 'e': 1, 'r': 1, 'i': 1, 'f': 2}
dic2 = {'s': 0, 'h': 0, 'e': 0, 'r': 0, 'i': 0, 'f': 0}
counter = 0
big_counter = 0
score = 0
for i in stroka:

    if i in word:
        counter += 1
        if i in stroka:
            index = stroka.index(i)

            stroka = stroka[:index] + "*" + stroka[index+1:]
            dic2[i] += 1
        #if counter == 7:
            score = 0
            for key in dic:

                if dic2[key] >= dic[key]:
                    score += 1
                    if score == 6:
                        big_counter += 1
                        score = 0
                        dic2.update({key: dic2.get(key, 0) - dic.get(key, 0) for key in dic})

            #big_counter += 1
            counter = 0
    else:
        pass
print(big_counter)




