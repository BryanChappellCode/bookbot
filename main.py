def sort_on(dict):
    return dict["num"]

def main():
    with open("./books/frankenstein.txt") as f:

        file_contents = f.read()

    words = file_contents.split()

    lowered_contents = file_contents.lower()

    letter_dict = {}

    for letter in lowered_contents:
        if letter not in letter_dict.keys():
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    letter_list = []

    for letter in letter_dict.keys():
        letter_list.append({"letter" : letter, "num" : letter_dict[letter]})

    letter_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    for entry in letter_list:
        if(entry['letter'].isalpha()):
            print(f"The '{entry['letter']}' character was found {entry['num']} times")


main()
