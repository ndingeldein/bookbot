def main():
    book_path = "books/frankenstein.txt"
    book_title = get_title(book_path)
    book_text = get_book_text(book_path)
    words_count = get_words(book_text)
    characters = get_characters(book_text)
    print(f"{book_title} has {words_count} words and the following characters:")
    print(characters)

def get_title(path):
    return path.split("/")[-1].split(".")[0]

def get_words(txt):
    return len(txt.split())

def get_characters(txt):
    characters = {}
    for char in txt:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
