def get_words(text_file):
    word_list = []
    f = open(text_file, 'r')
    for line in f:
        for word in line.split():
            word_list.append(word.strip())
    return word_list