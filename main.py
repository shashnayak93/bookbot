def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return file_contents

def count():
    words = main().split()
    return len(words)

def letter_dict():
    letter_dict = {}
    book = main().lower()
    for letter in book:
        if letter_dict.get(letter) == None:
            letter_dict[letter] = book.count(letter)
        else:
            continue
    
    return letter_dict

def report():
    report = f"--- Begin report of books/frankenstein.txt ---\n"
    report += f"{count()} words found in the document\n\n"

    letters = letter_dict()
    for letter, number in letters.items():
        if ord(letter)>=ord('a') and ord(letter)<=ord('z'):
            report+=f"The '{letter}' character was found {number} times\n"

    report+="--- End report ---"

    return report

print(report())