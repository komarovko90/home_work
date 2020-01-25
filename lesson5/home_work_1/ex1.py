f = open('text.txt', 'a', encoding='utf-8')

while True:
    word = input('Enter text or press "Enter" to end: ')
    if word == '':
        break
    f.write(word+'\n')

f.close()
