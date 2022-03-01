import pandas as pd

#TODO 1. Create a dictionary in this format:
data = pd.read_csv("nato_phonetic_alphabet.csv")
npa = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
loop = True
while loop:
    answer = input("Enter a word: ")
    answer=answer.upper()
    """new_list=[]
    for i in answer:
        temp_list=[row.code for (index, row) in data.iterrows() if i == row.letter]
        new_list += temp_list
    
    print(new_list)
    """

    try:
        phonetic_code = [npa[letter] for letter in answer]
        loop =False
    except:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(phonetic_code)




