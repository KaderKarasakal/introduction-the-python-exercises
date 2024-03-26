#dosyadan okuma ve işleme
def process_file(filename):

    words_list = list()
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word not in words_list:
                    words_list.append(word)

    words_list.sort()
    return words_list

filename = 'romeo.txt'

resulting_words = process_file(filename)
print(resulting_words)




