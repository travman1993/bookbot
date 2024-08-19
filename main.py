def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)

    report(word_count, letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    letter_freq = {}

    for char in text:
        if char.isalpha():
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1
    sorted_letter = sorted(
        [{'char': char, 'num': count} for char, count in letter_freq.items()],
        key=lambda x: x['num'],
        reverse=True,
    )
    return sorted_letter

def report(word_count, letter_count):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for item in letter_count:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print(f"--- End report ---")

main()

