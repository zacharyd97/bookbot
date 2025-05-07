def get_word_count(file):
    with open(file) as f:
        file_contents = f.read()
        split_text = file_contents.split()
        num_words = len(split_text)
        return num_words

def get_chars(file):
    with open(file) as f:
        file_contents = f.read()
        lowercase = file_contents.lower()
        char = {}

        for letters in lowercase:
            char[letters] = 0

        for letters in lowercase:
            char[letters] += 1
        return char

def sortable_dict(character):
    sortable_list = []
    for char in character:
        if char.isalpha() == True:
            sortable_list.append({"item":char, "num":character[char]})
    return sortable_list



def sort_on(dict):
    return dict["num"]
    