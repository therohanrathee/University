import string
def word_frequency(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

text = "Hello, all! Hello, everyone. My name is Aditya, Aditya Bhatia."
print(word_frequency(text))