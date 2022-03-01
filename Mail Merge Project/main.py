#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Getting names and creating the dictionary of the names
with open("./Input/Names/invited_names.txt") as file:
    a = file.readlines()
    name_list=[]
    for item in a:
        item = item.strip("\n")
        name_list.append(item)


for item in name_list:
    # reading the letter template
    with open("./Input/Letters/starting_letter.txt") as file2:
        a = file2.readlines()
        for i in a:
            # adding the invited names to the letters
            if "[name]" in i:
               i = "Dear " + item
               # saving the letter to the ready to send file
               with open("./Output/ReadytoSend/letter_for_" + item, 'w') as f:
                   f.write(i)
                   f.write("\n")
                   for line in a[1:]:
                       f.write(line)




