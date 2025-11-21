from stats import count_words
import sys
from stats import get_character_count

def get_book_text(filepath):
    with open(filepath,"r") as f:
        return f.read()

def main():
    if len(sys.argv)==2:
       data=get_book_text(sys.argv[1])

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(data)} total words")
    print("--------- Character Count -------")
    characters=get_character_count(data)
    sorted_item_desc=sorted(characters.items(),key=lambda item:item[1],reverse=True)
    sorted_dict=dict(sorted_item_desc)
    for key,value in sorted_dict.items():
        if key.isalpha():
           print(f"{key}: {value}")
main()
