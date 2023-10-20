with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    letter_dict = {}
    file_contents = file_contents.replace(" ", "")
    file_contents = file_contents.replace("\n", "")
    file_contents = file_contents.replace("\t", "")

    for letter in file_contents:
        if letter.lower() in letter_dict:
            letter_dict[letter.lower()] += 1
        else:
            letter_dict[letter.lower()] = 1

    print(letter_dict)
