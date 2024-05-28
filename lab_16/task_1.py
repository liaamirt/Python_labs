import nltk
import matplotlib.pyplot as plt
import string
import re
from nltk.corpus import stopwords
from collections import Counter

def MostUsed(text):
    words = nltk.word_tokenize(text)
    counted_words = Counter(words)

    most_used = counted_words.most_common(10)
    print(most_used)
    
    x = ["'" + most_used[i][0] + "'" for i in range(len(most_used))]
    y = [most_used[i][1] for i in range(len(most_used))]
    
    plt.rcParams['figure.figsize'] = (7, 5)
    plt.bar(x, y)
    plt.xlabel("words")
    plt.title("Без видалення з тексту стоп-слів")
    plt.show()
    
    clear_words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    stop_words.add("'s")
    
    clear_words = [x for x in clear_words if not re.fullmatch('[' + string.punctuation + ']+', x)]
    clear_words = [word for word in clear_words if not word in stop_words]
    counted_words = Counter(clear_words)
    
    most_used = counted_words.most_common(10)    
    print(most_used)
   
    x = ["'" + most_used[i][0] + "'" for i in range(len(most_used))]
    y = [most_used[i][1] for i in range(len(most_used))]
    
    plt.bar(x, y)
    plt.xlabel("words")
    plt.title("З видаленням")
    plt.show()

def CountWords(text):
    sentences = nltk.sent_tokenize(text)
    count_words = 0

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        count_words += len(words)

    return count_words


file = open("austen-emma.txt", "r")
text = file.read()

print("Кількість слів у тексті = ", CountWords(text))
MostUsed(text)

