import sys

if len(sys.argv) == 1 or sys.argv[1] == "":
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import ( 
    get_num_words, 
    char_counter, 
    to_be_sorted
)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = char_counter(text)
    chars_sorted_list = to_be_sorted(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")    

main()