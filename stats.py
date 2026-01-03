def number_of_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def count_each_character(text):
    character_count = {}
    for char in text:
        to_lower_char = char.lower()
        if to_lower_char in character_count:
            character_count[to_lower_char] += 1
        else:
            character_count[to_lower_char] = 1
    
    return character_count

def report_part1():
    print("============ BOOKBOT ============" + "Analyzing book found at books/frankstein.txt...\n" + "----------- Word Count ----------\n")

def report_part2(character_count):
    print("-------- Character Count --------")
    for char, count in character_count.items():
        print(f"{char}: {count}")
    print("============= END ===============")
    return ""