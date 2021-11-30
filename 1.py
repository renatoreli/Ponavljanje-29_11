#%%

import random

class NumberGuesser:
    def __init__(self) -> None:
        self.random_interval_numbers = [random.randint(0,1000) for x in range(5,10)]
        self.random_number = self.random_interval_numbers[len(self.random_interval_numbers)// 2]
        self.number_of_guesses = 0
        print(self.random_number)
        self.last_guessed_number = None

    def ask_user_to_guess_number(self):
        while True:
            user_guess_number = int(input("Unesite nasumični broj: "))
            self.number_of_guesses += 1
            is_in_range = self.check_user_guess_in_range(user_guess_number)
            if is_in_range:
                has_user_guessed_number = user_guess_number == self.random_number
                if has_user_guessed_number:
                    print("Broj pogođen")
                    print("Broj pokušaja:", self.number_of_guesses)
                    break
                else:
                    if self.last_guessed_number:
                        diff_last_guest_number = abs(self.last_guessed_number - self.random_number)
                        diff_current_guest_number = abs(user_guess_number - self.random_number)
                        if diff_current_guest_number < diff_last_guest_number:
                            print("Toplije")
                        else: print("Toplo")
                    else:
                        print("Toplo")
            else:
                print("Hladno")

            self.last_guessed_number = user_guess_number

    def check_user_guess_in_range(self, number: int):
        return number >= 0 and number <= 1000


numberGuesser = NumberGuesser()
numberGuesser.ask_user_to_guess_number()
# %%
#7
dnk1=input("Unesi prvi DNK: ")
dnk2=input("Unesi drugi DNK: ")

if len(dnk1) != len(dnk2):
    print("DNK se treba podudarat")

compared=[]

for i in range(len(dnk1)):
    dnk_char_1=dnk1[i]
    dnk_char_2=dnk2[i]

    if dnk_char_1 != dnk_char_2:
        compared.append((dnk_char_1,dnk_char_2))
print("razlika dva stringa su:", len(compared))
print("Parovi su:")
for compare in compared:
    print(compare)

# %%
#5
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,"q":10,
          "x": 8, "z": 10}
class Game:
    def generate_acronym(self,sentence: str):
        sentence: list[str] = sentence.split()
        if len(sentence) < 3:
            print("Atleast 3 words needed to continue")
            return

        sortedsent= sorted(sentence, key=len)[-3:]
        print(sorted)
        return ''.join(word[0] for word in sortedsent)

    def count_words(self,sentence):
        sentence: list[str] = sentence.split()
        words_in_sentence={}
        for word in sentence:
            word_exists= words_in_sentence.get(word) != None
            if word_exists:
                words_in_sentence[word] += 1
            else:
                words_in_sentence[word] = 1
        return words_in_sentence
    def scrabble_score(self,word):
        return sum(score[letter] for letter in word)
    
    def random(self,broj:int):
        final=""
        if broj%3==0:
            final+="pling"
        if broj%5==0:
            final+="plang"
        if broj%7==0:
            final+="plong"
        
        return final
        


scrabble=Game()
print(scrabble.generate_acronym("You Only Live Once"))   
print(scrabble.count_words("Yes No Yes No Yes No yes no yes no"))
print(scrabble.scrabble_score("aeuiosfdadfsajhfsda"))
print(scrabble.random(105))
# %%
