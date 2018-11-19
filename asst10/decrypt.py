# Maxwell Richard Tamer-Mahoney ID #: 201804029

import string, time

class WordCounter:
    def __init__(self, word_dictionary_file):
        with open(word_dictionary_file, 'r') as file:
            self.word_dictionary = file.readline().split()

    def count(self, string):
        possible_words = string.split()
        word_count = 0
        for pw in possible_words:
            pw.strip(' !@#$%^&*()-_+={}[]|\:;\'<>?,./"')
            pw.lower()
            if pw in self.word_dictionary:
                word_count += 1
        return word_count

class EncryptedMessage:
    def __init__(self, encrypted_text):
        self.encrypted_text = encrypted_text
    
    def build_shift_dict(self, shift):
        shift_dict = {}
 
        for cur_position in range(len(string.ascii_lowercase)):
            shifted_position = cur_position + shift if cur_position + shift <= 25 else cur_position + shift - 26
            shift_dict[string.ascii_lowercase[cur_position]] = string.ascii_lowercase[shifted_position]

        for cur_position in range(len(string.ascii_uppercase)):
            shifted_position = cur_position + shift if cur_position + shift <= 25 else cur_position + shift - 26
            shift_dict[string.ascii_uppercase[cur_position]] = string.ascii_uppercase[shifted_position]

        return shift_dict

    def apply_shift(self, shift):
        shift_dict = self.build_shift_dict(shift)
        shifted_string = ''
        for char in self.encrypted_text:
            shifted_string += shift_dict.get(char) if char.isalpha() else char
        return shifted_string

    def brute_force(self):
        WC = WordCounter('words.txt')

        possible_decryptions = {}

        for i in range(26):
            possible_decryptions[self.apply_shift(i)] = i

        best_shift = None
        best_shift_word_count = 0
        best_shift_result = None

        for pd, shift in possible_decryptions.items():
            pd_word_count = WC.count(pd)
            if pd_word_count > best_shift_word_count:
                best_shift = shift
                best_shift_word_count = pd_word_count
                best_shift_result = pd

        return (best_shift, best_shift_result)

if __name__ == '__main__':
    with open('story.txt', 'r') as file:
        story = file.read()

    my_message = EncryptedMessage(story)

    start = time.time()
    print(my_message.brute_force())
    end = time.time()

    print(f'Brute forced message in {end - start} seconds.')
