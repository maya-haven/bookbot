with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    print(file_contents)
    letters = letter_count(file_contents)
    words = word_count(file_contents)
    print(f'There are {words} words in this book')
    pre_sort = make_pretty(letters)
    pre_sort.sort(reverse=True, key=sort_key)
    for dictionary in pre_sort:
        print(f'The {dictionary['name']} character was found {dictionary['num']} times :3')

def sort_key(dict):
    return dict['num']

def letter_count(book: str) -> dict:
    lowered_book = book.lower()
    final_dict = dict()
    for character in lowered_book:
        if character.isalpha():
            final_dict[character] = final_dict.get(character, 0) + 1
    return final_dict

def word_count(book: str) -> int: 
    words = book.split()
    return len(words)

def make_pretty(data: dict):
    dict_list = []
    for name in data:
        ammount = data[name]
        dict_list.append({'name': name, 'num': ammount})
    return dict_list

if __name__ == "__main__":
    main()