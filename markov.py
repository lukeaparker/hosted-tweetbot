from dictogram import Dictogram
import utils
import random 
import os 
# import app
from pprint import pprint


class Markov2nd(Dictogram):
    def build_markov_2nd(self, file_name):
        self.word_list = utils.get_words(file_name)
        for sentence in self.word_list:
            self.build_sentence(sentence)

    
    def build_sentence(self, sentence):
        next_word_index = 0
        next_next_word_index = 1
        words = "i like dogs and you like dogs i like cats but you hate cats"
        for _ in range(2):
            sentence.insert(0, '$START$')
        for word in sentence:
            next_word_index += 1
            next_next_word_index += 1 
            if next_next_word_index >= len(sentence):
                break 
            if next_word_index < len(sentence):
                next_word = sentence[next_word_index]                    
            if next_next_word_index < len(sentence):
                next_next_word = sentence[next_next_word_index]
            pair = (word, next_word)
            if pair not in self:
                self[pair] = Dictogram()
            if pair in self:
                self[pair].add_count(next_next_word) 
        return self


    def sample_markov(self):
        previous = "$START$"
        current = "$START$"
        sentence = []

        while current != '$END$':
            next_word = self[(previous, current)].sample()
            previous = current
            current = next_word
            if current != '$END$': 
                sentence.append(next_word)
            elif current == '$END$':
                break
        return " ".join(sentence)




            




            