from stats import *
import sys

def get_book_text(filepath):
	file_contents = None
	with open(filepath) as file:
		file_contents = file.read()
	return file_contents

# Print everything out, i.e. print the final output of the prog
def print_output(wc, sorted_count):
	# Print the heading
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	# Print the word count
	print_word_count(wc)
	# Print the char count
	print_char_list(sorted_count)
	# Print footer
	print("============= END ===============")

# Prints word count along with a nice heading
def print_word_count(wc):
	print("----------- Word Count ----------")
	print(f"Found {wc} total words")

# Takes a list of dictionaries which store the char and the num of its occurance
# Prints them all out, each on its own separate line, starting with this heading:
# --------- Character Count -------
def print_char_list(sorted_count):
	print("--------- Character Count -------")
	for item in sorted_count:
		if item["char"].isalpha():
			print(f'{item["char"]}: {item["num"]}')

def main():
	filename = "str"

	# Check CLI arguments
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		filename = sys.argv[1]

	text = get_book_text(filename)
	# num of words in the text
	wc = word_count(text)
	# counts for various chars in the text
	character_count = char_count(text)
	# same counts, but formated as a list of dicts, where each entry, i.e. each
	# dict, has the format "char": 'x', "num": count
	sorted_count = sort_count(character_count)

	# Output to screen
	print_output(wc, sorted_count)

main()
