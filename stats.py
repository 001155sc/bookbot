def word_count(text):
	words = text.split()
	wc = len(words)
	return wc

def char_count(text):
	text = text.lower()
	char_count = {
		"a": 0,
		"b": 0,
		"c": 0,
		"d": 0,
		"e": 0,
		"f": 0,
		"g": 0,
		"h": 0,
		"i": 0,
		"j": 0,
		"k": 0,
		"l": 0,
		"m": 0,
		"n": 0,
		"o": 0,
		"p": 0,
		"q": 0,
		"r": 0,
		"s": 0,
		"t": 0,
		"u": 0,
		"v": 0,
		"w": 0,
		"x": 0,
		"y": 0,
		"z": 0,
		"0": 0,
		"1": 0,
		"2": 0,
		"3": 0,
		"4": 0,
		"5": 0,
		"6": 0,
		"7": 0,
		"8": 0,
		"9": 0,
		".": 0,
		",": 0,
		"!": 0,
		"?": 0,
		"£": 0,
		"$": 0,
		"%": 0,
		"^": 0,
		"&": 0,
		"*": 0,
		"(": 0,
		")": 0,
		"_": 0,
		"-": 0,
		"+": 0,
		"=": 0,
		"[": 0,
		"]": 0,
		"{": 0,
		"}": 0,
		":": 0,
		";": 0,
		"@": 0,
		"~": 0,
		"#": 0,
		"<": 0,
		">": 0,
		"/": 0,
		"|": 0
	}

	for char in text:
		if char in char_count:
			char_count[char] += 1

	return char_count



def sort_count(char_count):
	# Tells the .sort() function which key to sort on? Not sure I understand how .sort() works
	def sort_on(dict):
		return dict["num"]

	# Creates a list of dictionaries whcih have the format {"char": "x", "num": num}
	def create_list(char_count):
		list = []
		for key in char_count:
			dict = {"char": key, "num": char_count[key]}
			list.append(dict)
		return list

	char_list = create_list(char_count)
	char_list.sort(reverse=True, key=sort_on)

	return char_list
