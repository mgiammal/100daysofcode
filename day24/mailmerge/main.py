# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    invited_list = names.readlines()
    invited_list = [x[:-1] for x in invited_list]
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_template = letter.read()
    for name in invited_list:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_to_send:
            letter_to_send.write(letter_template.replace(PLACEHOLDER, name))
