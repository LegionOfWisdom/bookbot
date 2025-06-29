def get_book_text(filepath):
    file_content = ''
    
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main():
    from stats import word_counter
    
    book_path = "/home/mbarrio/workspace/github.com/LegionOfWisdom/bookbot/books/frankenstein.txt"
    num_words = 0
    
    content = get_book_text(book_path)
    num_words = word_counter(content)
    
    print (f"{num_words} words found in the document")

main ()