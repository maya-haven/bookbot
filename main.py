with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    print(file_contents)
    print(letter_count(file_contents))
    print(split_the_whitespace(file_contents))

def letter_count(book: str) -> str:
    lowered_book = book.lower()
    final_dict = dict()
    for character in lowered_book:
        if character.isalpha() is True:
            final_dict[character] = final_dict.get(character, 0) + 1
    return final_dict

def split_the_whitespace(bookington: str) -> str: 
    words = bookington.split()
    return len(words)

if __name__ == "__main__":
    main()