def get_words(text_file):
    sentence_list = []
    f = open(text_file, 'r')
    for line in f:
        word_list = []
        for word in line.split():
            word_list.append(word.strip())
        word_list.append('$END$')
        sentence_list.append(word_list)
    return sentence_list