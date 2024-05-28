def swap_first_last_words(sentence):
    words = sentence.split()

    if len(words) < 2:
        return sentence

    words[0], words[-1] = words[-1], words[0]

    new_sentence = ' '.join(words)
    return new_sentence


sentence = input("Введіть речення: ")    
new_sentence = swap_first_last_words(sentence)    
print("Нове речення:", new_sentence)
