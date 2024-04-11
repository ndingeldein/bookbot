def main():
    book_path = "books/frankenstein.txt"
    book_title = get_title(book_path)
    book_text = get_book_text(book_path)
    words_count = get_words(book_text)
    characters = get_characters(book_text)

    print(f"--- Begin report of {book_path} ---\n")
    print(f"{words_count} words found in {book_title}")
    for character in get_character_list(characters):
        print(f"The {character['char']} character appears {character['count']} times")

    print(f"\n--- End report of {book_path} ---")

def get_title(path):
    return path.split("/")[-1].split(".")[0]

def get_words(txt):
    return len(txt.split())

def get_characters(txt):
    characters = {}
    for char in txt:
        if char.isalpha():
            lowercased = char.lower()
            if lowercased in characters:
                characters[lowercased] += 1
            else:
                characters[lowercased] = 1
    return characters

def get_character_list(characters):
    character_list = []
    for char in characters:
        character_list.append({
            "char": char,
            "count": characters[char]
        })
    character_list.sort(reverse=True, key=sort_characters)
    return character_list

def sort_characters(characters):
    return characters["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
