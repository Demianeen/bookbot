def main():
    content_path = "./books/frankenstein.txt"
    book_report(content_path)


def sort_on(tuple):
    return tuple[1]


def book_report(content_path):
    file_content = get_file_content(content_path)
    words_count = count_words(file_content)
    char_dict = get_letters_dict(file_content)

    print(f"--- Begin report of {content_path} ---")
    print(f"{words_count} words found in the document\n")

    char_array = list(char_dict.items())
    char_array.sort(reverse=True, key=sort_on)

    for char, count in char_array:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_letters_dict(string):
    lowercase_string = string.lower()
    char_dict = {}
    for char in lowercase_string:
        try:
            char_dict[char] += 1
        except KeyError:
            char_dict[char] = 1
    return char_dict


def count_words(string):
    return len(string.split())


def get_file_content(content_path):
    with open(content_path) as f:
        return f.read()


main()
