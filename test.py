def read_qustion():
    quest = []
    with open('bot_text1.txt', 'r', encoding='utf-8') as file:
        for line in file:
            quest += [line.strip()]
        return quest

a = read_qustion()

print(a)
