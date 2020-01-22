with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    print('-'*20)
    f.seek(0)
    print(f.read())
    print('-' * 20)
    print(f'Number of lines: {len(text)}')
    count_words = 0
    for num, el in enumerate(text):
        words = el.split()
        print(f'Number of words per line {num+1}: {len(words)}')
        count_words += len(words)
    print(f'Number of words in file: {count_words}')
