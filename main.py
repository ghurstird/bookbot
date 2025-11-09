from stats import get_word_count, get_char_count, get_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    try:
        book_text = get_book_text(sys.argv[1])
    except FileNotFoundError:
        print(f"\nERROR> Couldnt find file: {sys.argv[1]}\n")    
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")

    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")

    print("--------- Character Count -------")
    sorted_char_counts = get_sorted_list(get_char_count(book_text))
    for dict in sorted_char_counts:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")    

    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
        
main()

