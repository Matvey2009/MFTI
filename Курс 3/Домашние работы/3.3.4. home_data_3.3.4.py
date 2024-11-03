def enumerate_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            words_dict = {index + 1: word for index, word in enumerate(words)}
            return words_dict
    except FileNotFoundError:
        return "Файл не найден"
