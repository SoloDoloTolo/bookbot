def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"The book contains {word_count} words.")

        # Convert the entire file content to lowercase
        lowered_string = file_contents.lower()
        
        char_count = {}

        for char in lowered_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        char_list = []

        for char, count in char_count.items():
            char_dict = {"character": char, "num": count}
            char_list.append(char_dict)

        # Define the sort function
        def sort_on(char_dict):
            return char_dict["num"]

        # Sort the list by the count in descending order
        char_list.sort(reverse=True, key=sort_on)

        # Print the filtered and formatted report
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        for item in char_list:
            if item["character"].isalpha():
                print(f"The '{item['character']}' character was found {item['num']} times")

        print("--- End report ---")

if __name__ == "__main__":
    main()