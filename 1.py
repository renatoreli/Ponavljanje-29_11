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
