import re
import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

file = open("A_great_summer_vacation.txt", "r")
output_file = open("Output_File.txt", "w")

text = file.read()
file.close()

print(text) 

words = nltk.casual_tokenize(text) 
print("\tТокенізація\n", words)

stop_words = set(stopwords.words("english"))
clear_words = [x for x in words if not re.fullmatch('[' + string.punctuation + ']+', x)] 
clear_words = [word for word in clear_words if not word in stop_words] 

print("\n\tВідібраний текст\n", ' '.join(clear_words))

ps = PorterStemmer()
root_words = list(map(ps.stem, clear_words))

print("\n\tСтемінг відібраного тексту \n", root_words)

wl = WordNetLemmatizer()
lem_words = list(map(wl.lemmatize, clear_words))

print("\n\tЛемматизація відібраного тексту \n", lem_words)

output_file.write("\tВідформатований текст \n" + ' '.join(root_words))
output_file.close()
