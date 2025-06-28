def get_book_text(filepath):
    file_content = ''
    
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main():
    content = get_book_text("/home/mbarrio/workspace/github.com/LegionOfWisdom/bookbot/books/frankenstein.txt")
    print (content)

main ()