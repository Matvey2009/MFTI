def the_longest(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
