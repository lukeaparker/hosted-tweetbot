from dictogram import Dictogram
import utils
import random 
import os 
import app


class Markov(Dictogram):
  
    def build_markov(self, file_name):
        previous = None
        self.word_list = utils.get_words(file_name) 
        for word in self.word_list:
            if previous is None:
                previous = word
                continue
            if previous not in self:
                self[previous] = Dictogram()
            self[previous].add_count(word) 
            previous = word
        print(self)
    
    # def after_word_list(self, word):
    #     i = 0 
    #     pword_list = []
    #     for pword in self.word_list:
    #         i += 1
    #         if pword == word and i < len(self.word_list):
    #             pword_list.append(self.word_list[i])  
    #     return pword_list



    
    def sample_markov(self):
        ranum = random.random() * len(self.word_list)
        word = self.word_list[int(ranum)]
        sentence = [word]
        while len(sentence) <= 15:
            word = self[word].sample() 
            sentence.append(word)
        return sentence
                
        
if __name__ == "__main__":
    mv = Markov()
    build = mv.build_markov()
    print(build)
    sample = mv.sample_markov()
    print(sample)
