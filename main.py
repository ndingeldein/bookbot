def main():
    book_path = "books/frankenstein.txt"
    book_title = get_title(book_path)
    book_text = get_book_text(book_path)
    words_count = get_words(book_text)
    print(f"{book_title} has {words_count} words.")

def get_title(path):
    return path.split("/")[-1].split(".")[0]

def get_words(txt):
    return len(txt.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
