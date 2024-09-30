def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The {item['char']} chracter was found {item['count']} times")

    print("--- End report ---")


def sort_on(dict):
    return dict["count"]


def get_book_text(path):
    with open(path) as file:
        return file.read()


def get_word_count(book):
    words = book.split()
    return len(words)


def get_chars_dict(book):
    characters = {}
    for char in book:
        lowered_char = char.lower()

        if lowered_char in characters:
            characters[lowered_char] += 1
        else:
            characters[lowered_char] = 1

    return characters


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "count": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
