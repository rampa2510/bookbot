with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    letter_dict = {}
    word_count = len(file_contents.split())
    file_contents = file_contents.replace(" ", "")
    file_contents = file_contents.replace("\n", "")
    file_contents = file_contents.replace("\t", "")

    for letter in file_contents:
        if letter.lower() in letter_dict:
            letter_dict[letter.lower()] += 1
        else:
            letter_dict[letter.lower()] = 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words by default")

    sorted_dict = sorted(
        letter_dict.items(), key=lambda character: character[1], reverse=True
    )

    for letter_data in sorted_dict:
        if letter_data[0].isalpha():
            print(f"character {letter_data[0]} is repeated {letter_data[1]} times")
