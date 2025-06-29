def get_book_text(filepath):
    file_content = ''
    
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main():
    book_path = "/home/mbarrio/workspace/github.com/LegionOfWisdom/bookbot/books/frankenstein.txt"
    num_words = 0
    
    content = get_book_text(book_path)
    ttl_words = len(content.split())
    
    print (f"{ttl_words} words found in the document")

main ()